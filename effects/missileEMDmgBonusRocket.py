#Used by: Item: Hardwiring - 'Snapshot' ZMRX
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusRocket(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Rockets", self.item)