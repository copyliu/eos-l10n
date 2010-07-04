#Used by: Item: Mindflood Booster
#               Exile Booster
type = "boosterSideEffect"
displayName = "Explosion Radius Penalty"
from customEffects import boostAmmoListBySkillReq
def boosterMissileExplosionCloudPenaltyFixed(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "aoeCloudSize", "boosterMissileAOECloudPenalty",
                            lambda skill: skill.name == "Missile Launcher Operation", self.item)