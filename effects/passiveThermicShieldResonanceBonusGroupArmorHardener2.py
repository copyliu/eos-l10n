#Used by: Skill: Thermic Shield Compensation
from customEffects import boostModListByReq, multiply
def passiveThermicShieldResonanceBonusGroupArmorHardener2(self, fitting, level):
    boostModListByReq(fitting.modules, "passiveThermicDamageResistanceBonus", "hardeningbonus2",
                           lambda mod: mod.group.name == "Shield Hardener",
                           self.item, extraMult = level, helper = multiply)
