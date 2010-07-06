#Used by: Item: Magnatar Effect Beacon
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemStandardMissileExplosiveDamage(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "smallWeaponDamageMultiplier",
                      lambda skill: skill.name == "Standard Missiles",
                      self.item, helper = multiply)