#Used by: Item: Magnetar Effect Beacon
type = "projected"
from customEffects import boostModListByReq, multiply
def systemTargetPaintingAmount(self, fitting, state):
    boostModListByReq(fitting.modules, "signatureRadiusBonus", "signatureRadiusBonusMultiplier",
                      lambda mod: mod.group.name == "Target Painter",
                      self.item, helper = multiply)