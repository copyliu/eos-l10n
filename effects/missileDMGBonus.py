#Items from group: Ballistic Control system (21 of 21) [Module]
from customEffects import boostAmmoListBySkillReq, multiply
import model.fitting
def missileDMGBonus(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostAmmoListBySkillReq(fitting.modules,
                               ("emDamage", "kineticDamage", "explosiveDamage", "thermalDamage"),
                                "missileDamageMultiplierBonus",
                                lambda skill: skill.name == "Missile Launcher Operation",
                                self.item, useStackingPenalty = True, helper = multiply)