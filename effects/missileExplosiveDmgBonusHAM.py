#Used by: Item: Hardwiring - 'Snapshot' ZMEX
from customEffects import boostAmmoListBySkillReq
def missileExplosiveDmgBonusHAM(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item)