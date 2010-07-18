#Items from group: Missile Launcher Operation (7 of 24)
from customEffects import boostAmmoListByReq
def missileKineticDmgBonus2(self, fitting, level):
    boostAmmoListByReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                           lambda charge: self.item in charge.requiredSkills,
                           self.item, extraMult = level)