#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
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

import re

from sqlalchemy.orm import reconstructor

from eqBase import EqBase

try:
    from collections import OrderedDict
except ImportError:
    from gui.utils.compat import OrderedDict

class Effect(EqBase):
    '''
    The effect handling class, it is used to proxy and load effect handler code,
    as well as a container for extra information regarding effects coming
    from the gamedata db.

    @ivar ID: the ID of this effect
    @ivar name: The name of this effect
    @ivar description: The description of this effect, this is usualy pretty useless
    @ivar published: Wether this effect is published or not, unpublished effects are typicaly unused.
    '''
    #Filter to change names of effects to valid python method names
    nameFilter = re.compile("[^A-Za-z0-9]")

    @reconstructor
    def init(self):
        '''
        Reconstructor, composes the object as we grab it from the database
        '''
        self.__generated = False
        self.handlerName = re.sub(self.nameFilter, "", self.name).lower()

    @property
    def handler(self):
        '''
        The handler for the effect,
        It is automaticly fetched from effects/<effectName>.py if the file exists
        the first time this property is accessed.
        '''
        if not self.__generated:
            self.__generateHandler()

        return self.__handler

    @property
    def runTime(self):
        '''
        The runTime that this effect should be run at.
        This property is also automaticly fetched from effects/<effectName>.py if the file exists.
        the possible values are:
        None, "early", "normal", "late"
        None and "normal" are equivalent, and are also the default.

        effects with an early runTime will be ran first when things are calculated,
        followed by effects with a normal runTime and as last effects with a late runTime are ran.
        '''
        if not self.__generated:
            self.__generateHandler()

        return self.__runTime

    @property
    def type(self):
        '''
        The type of the effect, automaticly fetched from effects/<effectName>.py if the file exists.

        Valid values are:
        "passive", "active", "projected", "gang"

        Each gives valuable information to eos about what type the module having
        the effect is. passive vs active gives eos clues about wether to module
        is activatable or not (duh!) and projected and gang each tell eos that the
        module can be projected onto other fits, or used as a gang booster module respectivly
        '''
        if not self.__generated:
            self.__generateHandler()

        return self.__type

    @property
    def isImplemented(self):
        '''
        Wether this effect is implemented in code or not,
        unimplemented effects simply do nothing at all when run
        '''
        return self.handler != effectDummy

    def isType(self, type):
        '''
        Check if this effect is of the passed type
        '''
        return self.type is not None and type in self.type

    def __generateHandler(self):
        '''
        Grab the handler, type and runTime from the effect code if it exists,
        if it doesn't, set dummy values and add a dummy handler
        '''
        try:
            self.__effectModule = effectModule = __import__('eos.effects.' + self.handlerName, fromlist=True)
            self.__handler = getattr(effectModule, "handler")
            try:
                self.__runTime = getattr(effectModule, "runTime") or "normal"
            except AttributeError:
                self.__runTime = "normal"

            try:
                t = getattr(effectModule, "type")
            except AttributeError:
                t = None

            t = t if isinstance(t, tuple) or t is None else (t,)
            self.__type = t
        except ImportError:
            self.__handler = effectDummy
            self.__runTime = "normal"
            self.__type = None

        self.__generated = True

    def getattr(self, key):
        if not self.__generated:
            self.__generateHandler()

        return getattr(self.__effectModule, key, None)

def effectDummy(*args, **kwargs):
    pass

class Item(EqBase):
    MOVE_ATTRS = (4,   # Mass
                  38,  # Capacity
                  161) # Volume

    MOVE_ATTR_INFO = None

    @classmethod
    def getMoveAttrInfo(cls):
        info = getattr(cls, "MOVE_ATTR_INFO", None)
        if info is None:
            cls.MOVE_ATTR_INFO = info = []
            import eos.db
            for id in cls.MOVE_ATTRS:
                info.append(eos.db.getAttributeInfo(id))

        return info

    def moveAttrs(self):
        self.__moved = True
        for info in self.getMoveAttrInfo():
            val = getattr(self, info.name, 0)
            if val != 0:
                attr = Attribute()
                attr.info = info
                attr.value = val
                self.__attributes[info.name] = attr

    @reconstructor
    def init(self):
        self.__race = None
        self.__requiredSkills = None
        self.__moved = False
        self.__offensive = None
        self.__assistive = None

    @property
    def attributes(self):
        if not self.__moved:
            self.moveAttrs()

        return self.__attributes

    def getAttribute(self, key):
        if key in self.attributes:
            return self.attributes[key].value

    def isType(self, type):
        for effect in self.effects.itervalues():
            if effect.isType(type):
                return True

        return False

    @property
    def requiredSkills(self):
        if self.__requiredSkills is None:
            # This import should be here to make sure it's fully initialized
            from eos import db
            requiredSkills = OrderedDict()
            self.__requiredSkills = requiredSkills
            # Map containing attribute IDs we may need for required skills
            # { requiredSkillX : requiredSkillXLevel }
            srqIDMap = {182: 277, 183: 278, 184: 279, 1285: 1286, 1289: 1287, 1290: 1288}
            combinedAttrIDs = set(srqIDMap.iterkeys()).union(set(srqIDMap.itervalues()))
            # Map containing result of the request
            # { attributeID : attributeValue }
            skillAttrs = {}
            # Get relevant attribute values from db (required skill IDs and levels) for our item
            for attrInfo in db.directAttributeRequest((self.ID,), tuple(combinedAttrIDs)):
                attrID = attrInfo[1]
                attrVal = attrInfo[2]
                skillAttrs[attrID] = attrVal
            # Go through all attributeID pairs
            for srqIDAtrr, srqLvlAttr in srqIDMap.iteritems():
                # Check if we have both in returned result
                if srqIDAtrr in skillAttrs and srqLvlAttr in skillAttrs:
                    skillID = int(skillAttrs[srqIDAtrr])
                    skillLvl = skillAttrs[srqLvlAttr]
                    # Fetch item from database and fill map
                    item = db.getItem(skillID)
                    requiredSkills[item] = skillLvl
        return self.__requiredSkills

    @property
    def race(self):
        if self.__race is None:
            # Define race map
            map = {1: "caldari",
                   2: "minmatar",
                   4: "amarr",
                   5: "sansha", # Caldari + Amarr
                   6: "blood", # Minmatar + Amarr
                   8: "gallente",
                   9: "guristas", # Caldari + Gallente
                   10: "angelserp", # Minmatar + Gallente, final race depends on the order of skills
                   16: "jove",
                   32: "sansha"} # Incrusion Sansha
            # Race is None by default
            race = None
            # Check if we're dealing with ORE ship first, using market group data
            if self.marketGroup and self.marketGroup.name == "ORE":
                race = "ore"
            # Check primary and secondary required skills' races
            if race is None:
                skills = self.requiredSkills.keys()
                skillPrimaryRace = (skills[0].raceID if len(skills) >= 1 else 0) or 0
                skillSecondaryRace = (skills[1].raceID if len(skills) >= 2 else 0) or 0
                skillRaces = (skillPrimaryRace, skillSecondaryRace)
                if sum(skillRaces) in map:
                    race = map[sum(skillRaces)]
                    if race == "angelserp":
                        if skillRaces == (2, 8):
                            race = "angel"
                        else:
                            race = "serpentis"

            # Rely on item's own raceID as last resort
            if race is None:
                race = map.get(self.raceID, None)

            # Store our final value
            self.__race = race
        return self.__race

    @property
    def assistive(self):
        """Detects if item can be used as assistance"""
        # Make sure we cache results
        if self.__assistive is None:
            assistive = False
            # Go through all effects and find first assistive
            for effect in self.effects.itervalues():
                if effect.info.isAssistance is True:
                    # If we find one, stop and mark item as assistive
                    assistive = True
                    break
            self.__assistive = assistive
        return self.__assistive

    @property
    def offensive(self):
        """Detects if item can be used as something offensive"""
        # Make sure we cache results
        if self.__offensive is None:
            offensive = False
            # Go through all effects and find first offensive
            for effect in self.effects.itervalues():
                if effect.info.isOffensive is True:
                    # If we find one, stop and mark item as offensive
                    offensive = True
                    break
            self.__offensive = offensive
        return self.__offensive

    def requiresSkill(self, skill, level=None):
        for s, l in self.requiredSkills.iteritems():
            if isinstance(skill, basestring):
                if s.name == skill and (level is None or l == level):
                    return True

            elif isinstance(skill, int) and (level is None or l == level):
                if s.ID == skill:
                    return True

            elif skill == s and (level is None or l == level):
                return True

            elif hasattr(skill, "item") and skill.item == s and (level is None or l == level):
                return True

        return False

class MetaData(EqBase):
    def __init__(self, name, val=None):
        self.fieldName = name
        self.fieldValue = val

class EffectInfo(EqBase):
    pass

class AttributeInfo(EqBase):
    pass

class Attribute(EqBase):
    pass

class Category(EqBase):
    pass

class Group(EqBase):
    pass

class Icon(EqBase):
    pass

class MarketGroup(EqBase):
    pass

class MetaGroup(EqBase):
    pass

class MetaType(EqBase):
    pass

class Unit(EqBase):
    pass
