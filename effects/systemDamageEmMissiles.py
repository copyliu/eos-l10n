#Used by: Item: Magnatar Effect Beacon
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemDamageEmMissiles(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierMultiplier",
                      lambda skill: skill.name == "Missile Launcher Operation",
                      self.item, helper = multiply)