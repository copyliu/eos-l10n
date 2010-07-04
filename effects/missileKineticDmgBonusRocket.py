#Used by: Item: Hardwiring - 'Snapshot' ZMRX
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusRocket(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Rockets", self.item)