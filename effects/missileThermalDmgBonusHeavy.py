#Used by: Item: Hardwiring - 'Snapshot' ZMHX
from customEffects import boostAmmoListBySkillReq
def missileThermalDmgBonusHeavy(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Missiles", self.item)