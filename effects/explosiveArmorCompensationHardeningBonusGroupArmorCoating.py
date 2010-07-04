#Used by: Skill: Explosive Armor Compensation
from customEffects import boostModListByReq
def explosiveArmorCompensationHardeningBonusGroupArmorCoating(self, fitting, level):
    boostModListByReq(fitting.modules, "explosiveDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Armor Coating",
                      self.item, extraMult = level)