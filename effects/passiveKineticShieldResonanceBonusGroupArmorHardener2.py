#Item: Kinetic Shield Compensation
from customEffects import boostModListByReq, multiply
def passiveKineticShieldResonanceBonusGroupArmorHardener2(self, fitting, level):
    boostModListByReq(fitting.modules, "passiveKineticDamageResistanceBonus", "hardeningbonus2",
                           lambda mod: mod.group.name == "Shield Hardener",
                           self.item, extraMult = level, helper = multiply)
