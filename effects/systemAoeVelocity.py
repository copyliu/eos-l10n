#Used by: Item: Magnatar Effect Beacon
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemAoeVelocity(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "aoeVelocityMultiplier",
                      lambda skill: skill.name == "Missile Launcher Operation",
                      self.item, helper = multiply)