#Item: Thermic Armor Compensation
from customEffects import boostModListByReq
def thermicArmorCompensationHardeningBonusGroupArmorCoating(self, fitting, level):
    boostModListByReq(fitting.modules, "thermalDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Armor Coating",
                      self.item, extraMult = level)