#Used by: Item: Hardwiring - 'Snapshot' ZMNX
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusStandard(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Standard Missiles", self.item)