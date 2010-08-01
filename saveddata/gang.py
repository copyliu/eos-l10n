#===============================================================================
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

from itertools import chain

class Gang(object):
    def calculateModifiedAttributes(self):
        #Make sure ALL fits in the gang have been calculated
        for c in chain(self.wings, (self.leader,)):
            if c != None: c.calculateModifiedAttributes()

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
            if c != None: c.calculateModifiedAttributes()

    def calculateGangBonusses(self, store):
        self.broken = False
        if self.leader == None:
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
        if self.leader == None:
            #Broken chain, don't boost up. And don't boost ourselves either.
            self.broken = True
        elif self.booster != None:
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
            self.bonusses[dictType] = {"ship": None}
            for boostType in ("skills", "modules"):
                self.bonusses[dictType][boostType] = {}

    def set(self, fit, layer):
        if fit == None:
            return

        dict = self.bonusses[layer]
        #Clear existing bonusses
        dict["ship"] = None
        dict["modules"].clear()
        dict["skills"].clear()


        for mod in fit.modules:
            if mod.item.isType("gang"):
                dict["modules"][mod.item.name] = mod

        for skill in fit.character.iterSkills():
            if skill.item.isType("gang"):
                dict["skills"][skill.item.name] = skill

        if fit.ship.item.isType("gang"):
            dict["ship"] = fit.ship
    def apply(self, fit, layer):
        skills = set()
        mods = set()
        ships = set()
        for dictType in ("fleet", "wing", "squad"):
            for skill in self.bonusses[dictType]["skills"].keys():
                skills.add(skill)

            for mod in self.bonusses[dictType]["modules"].keys():
                mods.add(mod)

            if self.bonusses[dictType]["ship"] != None:
                ships.add(self.bonusses[dictType]["ship"].item.name)

        #Run through skills
        for skillName in skills:
            skill = self.getHighestBonus(layer, "skills", skillName)
            if skill == None: continue
            for effect in skill.item.effects.values():
                for runTime in ("early", "normal", "late"):
                    if effect.isType("gang") and effect.runTime == runTime:
                        try:
                            effect.handler(fit, skill, ("gang", "skill"))
                        except AttributeError:
                            pass

        #Do the ship
        for shipName in ships:
            ship = self.getHighestBonus(layer, "ship", shipName)
            if ship == None: continue
            for effect in ship.item.effects.values():
                for runTime in ("early", "normal", "late"):
                    if effect.isType("gang") and effect.runTime == runTime:
                        try:
                            effect.handler(fit, ship, ("gang", "ship"))
                        except AttributeError:
                            pass

        #And the modules
        for modName in mods:
            mod = self.getHighestBonus(layer, "modules", modName)
            if mod == None: continue
            for effect in mod.item.effects.values():
                for runTime in ("early", "normal", "late"):
                    if effect.isType("gang") and effect.runTime == runTime:
                        try:
                            effect.handler(fit, mod, ("gang", "module"))
                        except AttributeError:
                            pass

    def getHighestBonus(self, layer, type, name = None):
        highestStuff = None
        highest = 0
        for dictType in ("fleet", "wing", "squad"):
            stuff = self.bonusses[dictType][type]
            if stuff == None:
                #Chain broken, only consider stuff under the current ones
                highest = 0
                highestStuff = None
                continue

            if type == "ship":
                if abs(highest) < abs(stuff.commandBonus) and stuff.item.name == name:
                    highest = stuff.commandBonus
                    highestStuff = stuff
            elif type == "skills":
                if name not in stuff: continue
                skill = stuff[name]
                if abs(highest) < abs(skill.commandBonus):
                    highest = skill.commandBonus
                    highestStuff = skill
            elif type == "modules":
                if name not in stuff: continue
                module = stuff[name]
                commandBonus = module.getModifiedItemAttr("commandBonus")
                if abs(highest) < abs(commandBonus):
                    highest = commandBonus
                    highestStuff = module
            if dictType == layer:
                return highestStuff