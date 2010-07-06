#Used by: Skill: EM Armor Compensation
from customEffects import boostModListByReq
def emArmorCompensationHardeningBonusGroupArmorCoating(self, fitting, level):
    boostModListByReq(fitting.modules, "emDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Armor Coating",
                      self.item, extraMult = level)