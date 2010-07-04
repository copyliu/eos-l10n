#Used by: Item: Hardwiring - 'Snapshot' ZMEX
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusHAM(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item)