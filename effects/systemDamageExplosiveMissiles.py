#Used by: Item: Magnatar Effect Beacon
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemDamageExplosiveMissiles(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierMultiplier",
                      lambda skill: skill.name == "Missile Launcher Operation",
                      self.item, helper = multiply)