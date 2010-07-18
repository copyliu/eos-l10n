#Item: Explosive Shield Compensation [Skill]
from customEffects import boostModListByReq, multiply
def passiveExplosiveShieldResonanceBonusGroupArmorHardener2(self, fitting, level):
    boostModListByReq(fitting.modules, "passiveExplosiveDamageResistanceBonus", "hardeningbonus2",
                           lambda mod: mod.group.name == "Shield Hardener",
                           self.item, extraMult = level, helper = multiply)
