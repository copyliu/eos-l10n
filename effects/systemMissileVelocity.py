#Used by: Item: Black Hole Effect Beacon
type = "projected"
from customEffects import boostAmmoListBySkillReq, multiply
def systemMissileVelocity(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "missileVelocityMultiplier",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, helper = multiply)