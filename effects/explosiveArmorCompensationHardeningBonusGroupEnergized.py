#Item: Explosive Armor Compensation
from customEffects import boostModListByReq
def explosiveArmorCompensationHardeningBonusGroupEnergized(self, fitting, level):
    boostModListByReq(fitting.modules, "explosiveDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Armor Plating Energized",
                      self.item, extraMult = level)