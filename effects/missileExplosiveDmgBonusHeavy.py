#Used by: Item: Hardwiring - 'Snapshot' ZMHX
from customEffects import boostAmmoListBySkillReq
def missileExplosiveDmgBonusHeavy(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Missiles", self.item)