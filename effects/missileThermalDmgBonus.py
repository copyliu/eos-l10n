#Used by: Skill: Rockets
#                Standard Missiles
#                FoF Missiles
#                Heavy Missiles
#                Torpedoes
#                Cruise Missiles
#                Heavy Assault Missiles
from customEffects import boostAmmoListByReq
def missileThermalDmgBonus(self, fitting, level):
    boostAmmoListByReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                           lambda ammo: self.item in ammo.requiredSkills,
                           self.item, extraMult = level)