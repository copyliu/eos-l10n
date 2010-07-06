#Used by: Item: Warhead Calefaction Catalyst
from customEffects import boostAmmoListBySkillReq, multiply
def missileDMGBonusPassive(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules,
                           ("emDamage", "kineticDamage", "explosiveDamage", "thermalDamage"),
                            "missileDamageMultiplierBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, useStackingPenalty = True, helper = multiply)