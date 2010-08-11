#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from sqlalchemy.orm import reconstructor


class Effect(object):
    #Filter to change names of effects to valid python method names
    nameFilter = dict(zip(map(ord, u'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'), u''))

    @reconstructor
    def init(self):
        self.__generated = False
        self.handlerName = self.name.translate(Effect.nameFilter)

    @property
    def handler(self):
        if not self.__generated:
            self.__generateHandler()

        return self.__handler

    @property
    def runTime(self):
        if not self.__generated:
            self.__generateHandler()

        return self.__runTime

    @property
    def type(self):
        if not self.__generated:
            self.__generateHandler()

        return self.__type

    def isType(self, type):
        return self.type is not None and type in self.type

    def __generateHandler(self):
        try:
            effectModule = __import__('eos.effects.' + self.handlerName, fromlist=True)
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


def effectDummy(*args, **kwargs):
    pass


class Item(object):
    @reconstructor
    def init(self):
        self.__race = None
        self.__requiredSkills = None

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
            from eos import db
            requiredSkills = {}
            self.__requiredSkills = requiredSkills
            for i in xrange(5):
                skillID, skillLevel = None, None
                skillID = self.getAttribute('requiredSkill%d' % i)
                skillLevel = self.getAttribute('requiredSkill%dLevel' % i)
                if skillID is None or skillLevel is None:
                    continue

                item = db.getItem(int(skillID))
                requiredSkills[item] = skillLevel

        return self.__requiredSkills

    @property
    def race(self):
        if self.__race is None:
            #There's a few hacks in how we look for this regarding to ships
            #I'll discuss each of them as we do it
            #1: If a ship belongs to the ORE market group, it'll be tagged as ORE
            if self.marketGroup and self.marketGroup.name == "ORE":
                return "ORE"

            #2: Items can only have a single raceID
            #   For pirate ships, we'll have to check the races of the skills
            skillRaces = set()

            skillRaces.add(self.raceID)
            for skill in self.requiredSkills.iterkeys():
                if skill.raceID is not None:
                    skillRaces.add(skill.raceID)

            #Now that we know what races the skills have, figure it out
            #Our map on how stuff works.
            map = {(1, 8): "guristas",
                   (1, 4): "sansha",
                   (2, 4): "blood",
                   (2, 8): "angelserp",
                   (1,): "caldari",
                   (2,): "minmatar",
                   (4,): "amarr",
                   (8,): "gallente"}

            for matcher, race in map.iteritems():
                match = True
                for raceID in skillRaces:
                    if not raceID in matcher:
                        match = False
                        break
                if match:
                    self.__race = race
                    break

            #3: Special handling for angel/serpentis
            if race == "angelserp":
                if self.raceID == 2:
                    self.__race = "angel"
                else:
                    self.__race = "serpentis"

        return self.__race

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

        return False


class Attribute(object):
    pass


class Category(object):
    pass


class Group(object):
    pass


class Icon(object):
    pass


class MarketGroup(object):
    pass


class MetaGroup(object):
    pass
