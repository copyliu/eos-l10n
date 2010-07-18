#Items from group: Effect Beacon (6 of 38)
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemRocketKineticDamage(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "smallWeaponDamageMultiplier",
                      lambda skill: skill.name == "Rockets",
                      self.item, helper = multiply)