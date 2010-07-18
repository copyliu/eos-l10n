#Variations of item: Large Drone Control Range Augmentor I (2 of 2) [Module]
#Variations of item: Medium Drone Control Range Augmentor I (2 of 2) [Module]
#Variations of item: Small Drone Control Range Augmentor I (2 of 2) [Module]
#Item: Electronic Warfare Drone Interfacing [Skill]
#Item: Scout Drone Operation [Skill]
from customEffects import increase
def scoutDroneOperationDroneRangeBonusModAddDroneControlDistanceChar(self, fitting, state = None, level = 1):
    increase(fitting.ship, "_droneControlRange", "droneRangeBonus", self.item, extraMult = level)
