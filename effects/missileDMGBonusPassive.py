#Variations of item: Large Warhead Calefaction Catalyst I (2 of 2) [Module]
#Variations of item: Medium Warhead Calefaction Catalyst I (2 of 2) [Module]
#Variations of item: Small Warhead Calefaction Catalyst I (2 of 2) [Module]
from customEffects import boostAmmoListBySkillReq, multiply
def missileDMGBonusPassive(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules,
                           ("emDamage", "kineticDamage", "explosiveDamage", "thermalDamage"),
                            "missileDamageMultiplierBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, useStackingPenalty = True, helper = multiply)