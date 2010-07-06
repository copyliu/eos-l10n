#Used by: Item: Hardwiring - 'Snapshot' ZMUX
from customEffects import boostAmmoListBySkillReq
def missileThermalDmgBonusCruise3(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Cruise Missiles", self.item)