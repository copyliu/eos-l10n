#Used by: Item: Ballistic Control System
from customEffects import boostAmmoListBySkillReq, multiply
import model.fitting
def missileDMGBonus(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostAmmoListBySkillReq(fitting.modules,
                               ("emDamage", "kineticDamage", "explosiveDamage", "thermalDamage"),
                                "missileDamageMultiplierBonus",
                                lambda skill: skill.name == "Missile Launcher Operation",
                                self.item, useStackingPenalty = True, helper = multiply)