#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemDamageEmMissiles(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierMultiplier",
                      lambda skill: skill.name == "Missile Launcher Operation",
                      self.item, helper = multiply)