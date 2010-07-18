#Item: Explosive Armor Compensation
from customEffects import boostModListByReq, multiply
def passiveExplosiveArmorResonanceBonusGroupArmorHardener2FIXED(self, fitting, level):
    boostModListByReq(fitting.modules, "passiveExplosiveDamageResistanceBonus", "hardeningbonus2",
                           lambda mod: mod.group.name == "Armor Hardener",
                           self.item, extraMult = level, helper = multiply)
