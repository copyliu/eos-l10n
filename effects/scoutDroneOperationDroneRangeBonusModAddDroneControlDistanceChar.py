#Variations of item: Large Drone Control Range Augmentor I (2 of 2)
#Variations of item: Medium Drone Control Range Augmentor I (2 of 2)
#Variations of item: Small Drone Control Range Augmentor I (2 of 2)
#Item: Electronic Warfare Drone Interfacing
#Item: Scout Drone Operation
from customEffects import increase
def scoutDroneOperationDroneRangeBonusModAddDroneControlDistanceChar(self, fitting, state = None, level = 1):
    increase(fitting.ship, "_droneControlRange", "droneRangeBonus", self.item, extraMult = level)
