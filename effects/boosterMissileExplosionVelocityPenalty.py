#Used by: Item: Blue Pill Booster
from customEffects import boostAmmoListBySkillReq
type = "boosterSideEffect"
def boosterMissileExplosionVelocityPenalty(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "boosterAOEVelocityPenalty",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item)