#Item: EM Armor Compensation [Skill]
from customEffects import boostModListByReq
def emArmorCompensationHardeningBonusGroupArmorCoating(self, fitting, level):
    boostModListByReq(fitting.modules, "emDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.item.group.name == "Armor Coating",
                      self.item, extraMult = level)