#Used by: Item: Hardwiring - 'Snapshot' ZMRX
from customEffects import boostAmmoListBySkillReq
def missileExplosiveDmgBonusRocket(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Rockets", self.item)