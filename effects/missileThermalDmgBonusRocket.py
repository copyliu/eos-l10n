#Used by: Item: Hardwiring - 'Snapshot' ZMRX
from customEffects import boostAmmoListBySkillReq
def missileThermalDmgBonusRocket(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Rockets", self.item)