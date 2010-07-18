#Items from group: Effect Beacon (6 of 38)
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemStandardMissileThermalDamage(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "smallWeaponDamageMultiplier",
                      lambda skill: skill.name == "Standard Missiles",
                      self.item, helper = multiply)