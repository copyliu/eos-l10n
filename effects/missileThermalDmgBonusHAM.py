#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Missile Implants (3 of 12)
from customEffects import boostAmmoListBySkillReq
def missileThermalDmgBonusHAM(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item)