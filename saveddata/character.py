#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================


from eos.effectHandlerHelpers import HandledItem
from eos.modifiedAttributeDict import ItemAttrShortcut
from sqlalchemy.orm import validates, reconstructor
from eos.types import Item
from copy import deepcopy
import sqlalchemy.orm.exc as exc
import eos.config
from eos import eveapi

class Character(object):
    __all5 = None
    __all0 = None

    @classmethod
    def getSkillList(cls):
        import eos.db
        return eos.db.getItemsByCategory("Skill")

    @classmethod
    def getAll5(cls):
        if cls.__all5 is None:
            try:
                import eos.db
                all5 = eos.db.getCharacter("All 5")
            except exc.NoResultFound:
                all5 = Character("All 5")
                for skill in cls.getSkillList():
                    all5.addSkill(Skill(skill, 5, True))

                eos.db.saveddata_session.add(all5)

            cls.__all5 = all5
        return cls.__all5

    @classmethod
    def getAll0(cls):
        if cls.__all0 is None:
            try:
                import eos.db
                all0 = eos.db.getCharacter("All 0")
            except exc.NoResultFound:
                all0 = Character("All 0")
                eos.db.saveddata_session.add(all0)

            cls.__all0 = all0
        return cls.__all0

    def __init__(self, name):
        self.name = name
        self.__owner = None
        self.__skills = []
        self.__skillIdMap = {}
        self.apiKey = None

    @reconstructor
    def init(self):
        self.__skillIdMap = {}
        for skill in self.__skills:
            self.__skillIdMap[skill.itemID] = skill

    def apiCharList(self):
        api = eveapi.EVEAPIConnection()
        auth = api.auth(userID=self.apiID, apiKey=self.apiKey)
        apiResult = auth.account.Characters()
        return map(lambda c: c.name, apiResult.characters)

    def apiFetch(self, charName):
        api = eveapi.EVEAPIConnection()
        auth = api.auth(userID=self.apiID, apiKey=self.apiKey)
        apiResult = auth.account.Characters()
        charID = None
        for char in apiResult.characters:
            if char.name == charName:
                charID = char.characterID

        if charID == None:
            return

        import eos.db
        sheet = auth.character(charID).CharacterSheet()
        del self.__skills[:]
        self.__skillIdMap.clear()
        for skillRow in sheet.skills:
            self.addSkill(Skill(skillRow["typeID"], skillRow["level"]))

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    def addSkill(self, skill):
        self.__skills.append(skill)
        self.__skillIdMap[skill.itemID] = skill

    def getSkill(self, item):
        if isinstance(item, basestring):
            import eos.db
            item = eos.db.getItem(item)

        ID = getattr(item, "ID", None)
        skill = self.__skillIdMap.get(ID if ID is not None else item)
        if skill:
            return skill

        if isinstance(item, int):
            import eos.db
            item = eos.db.getItem(item)

        if item.category.name == "Skill":
            s = Skill(item, 0, False, False)
            self.addSkill(s)
            return s

    def iterSkills(self):
        return self.__skills.__iter__()

    def filteredSkillIncrease(self, filter, *args, **kwargs):
        for element in self.iterSkills():
            if filter(element):
                element.increaseItemAttr(*args, **kwargs)

    def filteredSkillMultiply(self, filter, *args, **kwargs):
        for element in self.iterSkills():
            if filter(element):
                element.multiplyItemAttr(*args, **kwargs)

    def filteredSkillBoost(self, filter, *args, **kwargs):
        for element in self.iterSkills():
            if filter(element):
                element.boostItemAttr(*args, **kwargs)

    def calculateModifiedAttributes(self, fit, runTime, forceProjected = False):
        if forceProjected: return
        for skill in self.iterSkills():
            skill.calculateModifiedAttributes(fit, runTime)

    def clear(self):
        for skill in self.iterSkills():
            skill.clear()

    def __deepcopy__(self, memo):
        copy = Character("%s copy" % self.name)
        copy.apiKey = self.apiKey
        copy.apiID = self.apiID
        for skill in self.iterSkills():
            copy.addSkill(Skill(skill.itemID, skill.level, False, skill.learned))

        return copy

    @validates("ID", "name", "apiKey", "ownerID")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "name" : lambda val: True,
               "apiKey" : lambda val: val is None or (isinstance(val, basestring) and len(val) == 64),
               "ownerID" : lambda val: isinstance(val, int)}

        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val

class Skill(HandledItem):
    def __init__(self, item, level = 0, ro = False, learned = True):
        self.__item = item if not isinstance(item, int) else None
        self.itemID = item.ID if not isinstance(item, int) else item
        self.__level = level if learned else None
        self.commandBonus = 0
        self.learned = learned
        self.build(ro)

    @reconstructor
    def init(self):
        self.build(False)
        self.learned = self.__level is not None
        self.__item = None

    def build(self, ro):
        self.__ro = ro
        self.__suppressed = False

    @property
    def level(self):
        if not self.learned: return 0
        else: return self.__level or 0

    @level.setter
    def level(self, level):
        if level < 0 or level > 5:
            raise ValueError(str(level) + " is not a valid value for level")

        if hasattr(self, "_Skill__ro") and self.__ro == True:
            raise ReadOnlyException()

        self.__level = level
        self.learned = True

    @property
    def item(self):
        if self.__item is None:
            import eos.db
            self.__item = eos.db.getItem(self.itemID)

        return self.__item

    def getModifiedItemAttr(self, key):
        return self.item.attributes[key].value

    def calculateModifiedAttributes(self, fit, runTime):
        if self.__suppressed or not self.learned: return
        for effect in self.item.effects.itervalues():
                if effect.runTime == runTime and effect.isType("passive"):
                    try:
                        effect.handler(fit, self, ("skill",))
                    except AttributeError:
                        continue

    def clear(self):
        self.__suppressed = False
        self.commandBonus = 0

    def suppress(self):
        self.__suppressed = True

    def isSuppressed(self):
        return self.__suppressed

    @validates("characterID", "skillID", "level")
    def validator(self, key, val):
        if hasattr(self, "_Skill__ro") and self.__ro == True and key != "characterID":
            raise ReadOnlyException()

        map = {"characterID": lambda val: isinstance(val, int),
               "skillID" : lambda val: isinstance(val, int)}

        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val

    def __deepcopy__(self, memo):
        copy = Skill(self.item, self.level, self.__ro)
        return copy

class ReadOnlyException(Exception):
    pass
