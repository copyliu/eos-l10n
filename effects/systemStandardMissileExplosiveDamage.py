#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemStandardMissileExplosiveDamage(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "smallWeaponDamageMultiplier",
                      lambda skill: skill.name == "Standard Missiles",
                      self.item, helper = multiply)