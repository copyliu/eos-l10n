#Used by: Skill: Rockets
#                Standard Missiles
#                FoF Missiles
#                Heavy Missiles
#                Torpedoes
#                Cruise Missiles
#                Heavy Assault Missiles
from customEffects import boostAmmoListByReq
def missileEMDmgBonus(self, fitting, level):
    boostAmmoListByReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                           lambda charge: self.item in charge.requiredSkills,
                           self.item, extraMult = level)