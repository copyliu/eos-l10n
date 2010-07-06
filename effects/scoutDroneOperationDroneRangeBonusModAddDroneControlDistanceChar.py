#Used by: Item: Drone Control Range Augmentor Rigs
#        Skill: Scout Drone Operation
#               Electronic Warfare Drone Interfacing
from customEffects import increase
def scoutDroneOperationDroneRangeBonusModAddDroneControlDistanceChar(self, fitting, state = None, level = 1):
    increase(fitting.ship, "_droneControlRange", "droneRangeBonus", self.item, extraMult = level)
