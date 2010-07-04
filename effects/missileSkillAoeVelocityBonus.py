#Used by: Skill: Target Navigation Prediction
#         Item : Warhead Flare Catalyst
#                Hardwiring - 'Deadeye' ZMSX
from customEffects import boostAmmoListBySkillReq
def missileSkillAoeVelocityBonus(self, fitting, level = 1, state = None):
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "aoeVelocityBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)