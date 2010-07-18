#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Missile Implants (3 of 12)
from customEffects import boostAmmoListBySkillReq
def missileExplosiveDmgBonusHeavy(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Missiles", self.item)