#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemRocketEmDamage(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "smallWeaponDamageMultiplier",
                      lambda skill: skill.name == "Rockets",
                      self.item, helper = multiply)