#Items from group: Effect Beacon (6 of 38)
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemStandardMissileEmDamage(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "smallWeaponDamageMultiplier",
                      lambda skill: skill.name == "Standard Missiles",
                      self.item, helper = multiply)