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

from itertools import chain
from eos.types import Skill, Module, Ship

class Fleet(object):
    def calculateModifiedAttributes(self):
        #Make sure ALL fits in the gang have been calculated
        for c in chain(self.wings, (self.leader,)):
            if c is not None: c.calculateModifiedAttributes()

        leader = self.leader
        self.booster = booster = self.booster if self.booster is not None else leader
        self.broken = False
        self.store = store = Store()
        store.set(booster, "fleet")
        #Go all the way down for each subtree we have.
        for wing in self.wings:
            wing.calculateGangBonusses(store)

        # Check skill requirements and wing amount to see if we break or not
        if len(self.wings) == 0 or leader is None or leader.character is None or leader.character.getSkill("Fleet Command").level < len(self.wings):
            self.broken = True

        #Now calculate our own if we aren't broken
        if self.broken == False:
            #We only get our own bonusses *Sadface*
            store.apply(leader, "fleet")

    def count(self):
        total = 0
        for wing in self.wings:
            total += wing.count()

        return total

class Wing(object):
    def calculateModifiedAttributes(self):
        for c in chain(self.squads, (self.leader,)):
            if c is not None: c.calculateModifiedAttributes()

    def calculateGangBonusses(self, store):
        self.broken = False
        leader = self.leader
        self.booster = booster = self.booster if self.booster is not None else leader

        store.set(booster, "wing")

        #ALWAYS move down
        for squad in self.squads:
            squad.calculateGangBonusses(store)

        # Check skill requirements and squad amount to see if we break or not
        if len(self.squads) == 0 or leader is None or leader.character is None or leader.character.getSkill("Wing Command").level < len(self.squads):
            self.broken = True

        #Check if we aren't broken, if we aren't, boost
        if self.broken == False:
            store.apply(leader, "wing")
        else:
            #We broke, don't go up
            self.gang.broken = True

    def count(self):
        total = 0 if self.leader is None else 1
        for squad in self.squads:
            total += squad.count()

        return total

class Squad(object):
    def calculateModifiedAttributes(self):
        for member in self.members:
            member.calculateModifiedAttributes()

    def calculateGangBonusses(self, store):
        self.broken = False
        leader = self.leader
        self.booster = booster = self.booster if self.booster is not None else leader
        store.set(booster, "squad")

        # Check skill requirements and squad size to see if we break or not
        if len(self.members) <= 1 or leader is None or leader.character is None or leader.character.getSkill("Leadership").level * 2 < len(self.members):
            self.broken = True

        if self.broken == False:
            for member in self.members:
                store.apply(member, "squad")
        else:
            self.wing.broken = True

    def count(self):
        return len(self.members)

class Store(object):
    def __init__(self):
        #Build our data containers
        self.bonusses = {}
        self.boosts = {}
        for dictType in ("fleet", "wing", "squad"):
            self.bonusses[dictType] = {}

    def set(self, fit, layer):
        if fit is None:
            return

        dict = self.bonusses[layer]
        #Clear existing bonusses
        dict.clear()

        for thing in chain(fit.modules, fit.character.iterSkills(), (fit.ship,)):
            for effect in thing.item.effects.itervalues():
                if effect.isType("gang"):
                    gangBoost = effect.getattr("gangBoost")
                    l = dict.get(gangBoost)
                    if l is None:
                        l = dict[gangBoost] = []

                    l.append((effect, thing))

    contextMap = {Skill: "skill",
                  Ship: "ship",
                  Module: "module"}

    def apply(self, fit, layer):
        if fit is None:
            return

        self.boosts[fit] = boosts = {}
        char = fit.character
        #Go through all different boosts, for each of them, figure what the fuck the highest one is
        for currLayer in ("fleet", "wing", "squad"):
            dict = self.bonusses[currLayer]
            for gangBoost, stuff in dict.iteritems():
                for info in stuff:
                    effect, thing = info
                    currBoost = boosts.get(gangBoost, (0,))[0]

                    bonus = effect.getattr("gangBonus") or "commandBonus"
                    skillName = effect.getattr("gangSkill")
                    newBoost = thing.getModifiedItemAttr(bonus) or 0
                    isSkill = type(thing) == Skill
                    if isSkill or (skillName is not None and char is not None):
                        skill = thing if isSkill else char.getSkill(skillName)
                        newBoost *= skill.level

                    if abs(newBoost) > abs(currBoost):
                        boosts[gangBoost] = (newBoost, info)

            #Don't look further down then current layer, wing commanders don't get squad bonusses and all that.
            if layer == currLayer:
                break

        self.modify(fit)

    def getBoosts(self, fit):
        return self.boosts.get(fit)

    def modify(self, fit):
        boosts = self.getBoosts(fit)
        #Now we got it all figured out, actualy do the useful part of all this
        for name, info in boosts.iteritems():
            effect, thing = info[1]
            context = ("gang", self.contextMap[type(thing)])
            try:
                effect.handler(fit, thing, context)
            except:
                pass
