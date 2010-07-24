#Item: Focused Warp Disruption [Charge]
from customEffects import boost
def scriptSignatureRadiusBonusBonus(self, fitting, containerModule):
    boost(containerModule, "signatureRadiusBonus", "signatureRadiusBonusBonus", self.item)
    
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("signatureRadiusBonus", module.getModifiedChargeAttr("signatureRadiusBonusBonus"))