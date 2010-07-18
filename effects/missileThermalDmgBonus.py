#Items from group: Missile Launcher Operation (7 of 24) [Skill]
from customEffects import boostAmmoListByReq
def missileThermalDmgBonus(self, fitting, level):
    boostAmmoListByReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                           lambda charge: self.item in charge.requiredSkills,
                           self.item, extraMult = level)