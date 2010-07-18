#Items from group: Effect Beacon (6 of 38)
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemRocketExplosiveDamage(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "smallWeaponDamageMultiplier",
                      lambda skill: skill.name == "Rockets",
                      self.item, helper = multiply)