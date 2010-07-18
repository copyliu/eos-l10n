#Item: Kinetic Armor Compensation [Skill]
from customEffects import boostModListByReq, multiply
def passiveKineticArmorResonanceBonusGroupArmorHardener2(self, fitting, level):
    boostModListByReq(fitting.modules, "passiveKineticDamageResistanceBonus", "hardeningbonus2",
                           lambda mod: mod.group.name == "Armor Hardener",
                           self.item, extraMult = level, helper = multiply)
