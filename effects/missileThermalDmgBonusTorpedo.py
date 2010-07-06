#Used by: Item: Hardwiring - 'Snapshot' ZMTX
from customEffects import boostAmmoListBySkillReq
def missileThermalDmgBonusTorpedo(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Torpedoes", self.item)