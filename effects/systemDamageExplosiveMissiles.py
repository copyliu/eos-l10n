#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemDamageExplosiveMissiles(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierMultiplier",
                      lambda skill: skill.name == "Missile Launcher Operation",
                      self.item, helper = multiply)