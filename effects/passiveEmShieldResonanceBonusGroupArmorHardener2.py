#Item: EM Shield Compensation
from customEffects import boostModListByReq, multiply
def passiveEmShieldResonanceBonusGroupArmorHardener2(self, fitting, level):
    boostModListByReq(fitting.modules, "passiveEmDamageResistanceBonus", "hardeningbonus2",
                           lambda mod: mod.group.name == "Shield Hardener",
                           self.item, extraMult = level, helper = multiply)
