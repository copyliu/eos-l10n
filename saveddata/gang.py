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
            wing.calculateGangBonusses(self.leader)

class Wing(object):
    def calculateModifiedAttributes(self):
        for c in chain(self.squads, (self.leader,)):
            c.calculateModifiedAttributes()

    def calculateGangBonusses(self, alternative):
        pass


class Squad(object):
    def calculateModifiedAttributes(self):
        for fit in self.members:
            fit.calculateModifiedAttributes()


class Store():
    def __init__(self):
        self.__skillStore = {}
        self.__moduleStore = {}
        self.__ship = None
        self.__shipBonus = None

    def reconsider(self, fit):
        #Ships:
        #Check the fit's ship's commandBonus
        #(it will be set as extraAttribute by effect)
        if fit.ship.item.isType("gang"):
            currBonus = self.__shipBonus if self.__shipBonus else 0
            newBonus = fit.extraAttributes["commandBonus"] if "commandBonus" in fit.extraAttributes else 0
            if newBonus > currBonus:
                self.__ship = fit.ship
                self.__shipBonus = fit.extraAttributes["commandBonus"]

        #Modules:
        #Loop through all the modules on the fit & check their commandBonus.
        #if higher  then current, use instead.
        gangModules = filter(lambda mod: mod.item.isType("gang"), fit.modules)
        for mod in gangModules:
            name = mod.item.name
            newCommandBonus = mod.getModifiedItemAttr("commandBonus")
            currCommandBonus = self.__moduleStore[name].getModifiedItemAttr("commandBonus") if name in self.__moduleStore else 0
            if (newCommandBonus > currCommandBonus):
                self.__moduleStore[name] = mod

        #Skills part
        #TODO: Handle this differently, handling with level doesn't gracefully handle mindlinks
        #Get all the gang skills the char has
        #Loop through all the gangSkills the char has and checks if any are higher then the current ones
        #If they're higher, use those instead.
        gangSkills = filter(lambda skill: skill.item.isType("gang"), fit.character.iterSkills())
        for skill in gangSkills:
            name = skill.item.name
            currLevel =  self.__skillStore[name].level if name in self.__skillStore else 0
            newLevel = skill.level
            if newLevel > currLevel:
                self.__SkillStore[name] = skill


    def apply(self, fit):
        for runTime in ("early", "normal", "late"):
            #Run through skills
            for skill in self.__skillStore.values():
                for effect in skill.item.effects:
                    if effect.isType("gang") and effect.runTime == runTime:
                        effect.handler(fit, self, ("gang", "skill"))

            #Do the ship
            if self.__ship:
                for effect in self.__ship.item.effects:
                    if effect.isType("gang") and effect.runTime == runTime:
                        effect.handler(fit, self, ("gang", "ship"))

            #And the modules
            for mod in self.__moduleStore.values():
                for effect in mod.item.effects:
                    if effect.isType("gang") and effect.runTime == runTime:
                        effect.handler(fit, self, ("gang", "module"))