#Used by: Item: Magnatar Effect Beacon
from customEffects import boostAmmoListBySkillReq, multiply
type = "projected"
def systemRocketExplosiveDamage(self, fitting, state):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "smallWeaponDamageMultiplier",
                      lambda skill: skill.name == "Rockets",
                      self.item, helper = multiply)