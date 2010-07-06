#Used by: Item: Hardwiring - 'Snapshot' ZMNX
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusStandard(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Standard Missiles", self.item)