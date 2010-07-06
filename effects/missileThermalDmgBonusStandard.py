#Used by: Item: Hardwiring - 'Snapshot' ZMNX
from customEffects import boostAmmoListBySkillReq
def missileThermalDmgBonusStandard(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Standard Missiles", self.item)