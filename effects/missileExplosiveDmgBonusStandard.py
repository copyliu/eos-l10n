#Used by: Item: Hardwiring - 'Snapshot' ZMNX
from customEffects import boostAmmoListBySkillReq
def missileExplosiveDmgBonusStandard(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Standard Missiles", self.item)