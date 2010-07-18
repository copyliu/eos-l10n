#Item: EM Armor Compensation [Skill]
from customEffects import boostModListByReq, multiply
def passiveEmArmorResonanceBonusGroupArmorHardener2(self, fitting, level):
    boostModListByReq(fitting.modules, "passiveEmDamageResistanceBonus", "hardeningbonus2",
                           lambda mod: mod.group.name == "Armor Hardener",
                           self.item, extraMult = level, helper = multiply)
