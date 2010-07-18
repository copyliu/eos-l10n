#Item: Thermic Armor Compensation [Skill]
from customEffects import boostModListByReq
def thermicArmorCompensationHardeningBonusGroupEnergized(self, fitting, level):
    boostModListByReq(fitting.modules, "thermalDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Armor Plating Energized",
                      self.item, extraMult = level)