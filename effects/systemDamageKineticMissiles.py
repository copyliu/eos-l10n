#Items from group: Effect Beacon (6 of 38)
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemDamageKineticMissiles(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierMultiplier",
                      lambda skill: skill.name == "Missile Launcher Operation",
                      self.item, helper = multiply)