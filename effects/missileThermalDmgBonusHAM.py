#Used by: Item: Hardwiring - 'Snapshot' ZMEX
from customEffects import boostAmmoListBySkillReq
def missileThermalDmgBonusHAM(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item)