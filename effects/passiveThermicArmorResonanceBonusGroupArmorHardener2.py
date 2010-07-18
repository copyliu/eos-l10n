#Item: Thermic Armor Compensation
from customEffects import boostModListByReq, multiply
def passiveThermicArmorResonanceBonusGroupArmorHardener2(self, fitting, level):
    boostModListByReq(fitting.modules, "passiveThermicDamageResistanceBonus", "hardeningbonus2",
                           lambda mod: mod.group.name == "Armor Hardener",
                           self.item, extraMult = level, helper = multiply)
