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

class Gang(object):
    def calculateModifiedAttributes(self):
        #Make sure ALL fits in the gang have been calculated
        for c in chain(self.wings, (self.leader,)):
            if c is not None: c.calculateModifiedAttributes()

        self.broken = False
        store = Store()
        store.set(self.leader, "fleet")
        #Go all the way down for each subtree we have.
        for wing in self.wings:
            wing.calculateGangBonusses(store)

        #No wings = BAD FC, You won't be getting any bonusses!
        if len(self.wings) == 0:
            self.broken = True

        #Now calculate our own if we aren't broken
        if self.broken == False:
            #We only get our own bonusses *Sadface*
            store.apply(self.leader, "fleet")

class Wing(object):
    def calculateModifiedAttributes(self):
        for c in chain(self.squads, (self.leader,)):
            if c is not None: c.calculateModifiedAttributes()

    def calculateGangBonusses(self, store):
        self.broken = False
        if self.leader is None:
            #Broken chain
            self.broken = True
        else:
            store.set(self.leader, "wing")

        #ALWAYS move down
        for squad in self.squads:
            squad.calculateGangBonusses(store)

        #No squads = BAD WC, No bonusses!
        if len(self.squads) == 0:
            self.broken = True

        #Check if we aren't broken, if we aren't, boost
        if self.broken == False:
            store.apply(self.leader, "wing")
        else:
            #We broke, don't go up
            self.gang.broken = True

class Squad(object):
    def calculateModifiedAttributes(self):
        for member in self.members:
            member.calculateModifiedAttributes()

    def calculateGangBonusses(self, store):
        self.broken = False
        if self.leader is None:
            #Broken chain, don't boost up. And don't boost ourselves either.
            self.broken = True
        elif self.booster is not None:
            store.set(self.booster, "squad")
        else:
            store.set(self.leader, "squad")

        if len(self.members) <= 1:
            self.broken = True

        if self.broken == False:
            for member in self.members:
                store.apply(member, "squad")
        else:
            self.wing.broken = True

class Store(object):
    def __init__(self):
        #Build our data containers
        self.bonusses = {}
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

        boosts = {}
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

        #Now we got it all figured out, actualy do the useful part of all this
        for name, info in boosts.iteritems():
            effect, thing = info[1]
            context = ("gang", self.contextMap[type(thing)])
            try:
                effect.handler(fit, thing, context)
            except:
                pass
