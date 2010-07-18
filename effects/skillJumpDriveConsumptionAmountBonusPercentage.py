#Item: Jump Fuel Conservation [Skill]
from customEffects import boost
def skillJumpDriveConsumptionAmountBonusPercentage(self, fitting, level):
    boost(fitting.ship, "jumpDriveConsumptionAmount", "consumptionQuantityBonusPercentage", self.item, extraMult = level)
