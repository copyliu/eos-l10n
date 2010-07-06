#Used by: Item: Hardwiring - 'Snapshot' ZMEX
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusHAM(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item)