from itertools import chain

class Gang(object):
    def calculateModifiedAttributes(self):
        #Make sure ALL fits in the gang have been calculated
        for c in chain(self.wings, (self.leader,)):
            c.calculateModifiedAttributes()

        store = Store()
        #Now that we're confident every fit has been figured.
        #A fleet commander always gets his own bonusses,so lets do just that.
        store.reconsider(self.leader)
        store.apply(self.leader)
        #Do the same, one level down.
        for wing in self.wings:
            wing.calculateGangBonusses(store)

class Wing(object):
    def calculateModifiedAttributes(self):
        for c in chain(self.squads, (self.leader,)):
            c.calculateModifiedAttributes()

    def calculateGangBonusses(self, store):
        store.reconsider(self.leader)
        store.apply(self.leader)
        for squad in self.squads:
            squad.calculateGangBonusses(store)


class Squad(object):
    def calculateModifiedAttributes(self):
        for fit in self.members:
            fit.calculateModifiedAttributes()

    def calculateGangBonusses(self, store):
        store.reconsider(self.booster)
        for member in self.members:
            store.apply(member)

class Store():
    def __init__(self):
        self.__skillStore = {}
        self.__moduleStore = {}
        self.__ship = None
        self.__dead = False
        self.__started = False

    def reconsider(self, fit):
        #Tricky stuff:
        #When we already have some skills, and the chain is broken (None gets passed)
        #We will scrap all bonusses.
        if (fit == None and self.__started == False) or self.__dead == True:
            return
        elif fit == None and self.__started == True:
            self.__dead = True
            return
        if fit == None:
            return

        self.__started = True
        #Ships:
        #Check the fit's ship's commandBonus
        #(it will be set as extraAttribute by effect)
        if fit.ship and fit.ship.item.isType("gang"):
            currBonus = self.__ship.commandBonus if self.__ship else 0
            newBonus = fit.ship.commandBonus
            if newBonus > currBonus:
                self.__ship = fit.ship

        #Modules:
        #Loop through all the modules on the fit & check their commandBonus.
        #if higher  then current, use instead.
        gangModules = filter(lambda mod: mod.item.isType("gang"), fit.modules)
        for mod in gangModules:
            name = mod.item.name
            newCommandBonus = abs(mod.getModifiedItemAttr("commandBonus"))
            currCommandBonus = abs(self.__moduleStore[name].getModifiedItemAttr("commandBonus")) if name in self.__moduleStore else 0
            if (newCommandBonus > currCommandBonus):
                self.__moduleStore[name] = mod

        #Skills part
        #Get all the gang skills the char has
        #Loop through all the gangSkills the char has and checks if any are higher then the current ones
        #If they're higher, use those instead.
        for skill in fit.character.iterSkills():
            if skill.item.isType("gang"):
                name = skill.item.name
                currBonus =  self.__skillStore[name].commandBonus if name in self.__skillStore else 0
                newBonus = skill.commandBonus
                if newBonus > currBonus:
                    self.__skillStore[name] = skill


    def apply(self, fit):
        if self.__dead == True or self.__started == False:
            return

        for runTime in ("early", "normal", "late"):
            #Run through skills
            for skill in self.__skillStore.values():
                for effect in skill.item.effects.values():
                    if effect.isType("gang") and effect.runTime == runTime:
                        effect.handler(fit, skill, ("gang", "skill"))

            #Do the ship
            if self.__ship:
                for effect in self.__ship.item.effects.values():
                    if effect.isType("gang") and effect.runTime == runTime:
                        effect.handler(fit, self.__ship, ("gang", "ship"))

            #And the modules
            for mod in self.__moduleStore.values():
                for effect in mod.item.effects.values():
                    if effect.isType("gang") and effect.runTime == runTime:
                        effect.handler(fit, mod, ("gang", "module"))