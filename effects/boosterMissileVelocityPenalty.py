#Used by: Item: Crash Booster
#               X-Instinct Booster
type = "boosterSideEffect"
from customEffects import boostAmmoListBySkillReq
def boosterMissileVelocityPenalty(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "boosterMissileVelocityPenalty",
                           lambda skill: skill.name == "Missile Launcher Operation",
                           self.item)