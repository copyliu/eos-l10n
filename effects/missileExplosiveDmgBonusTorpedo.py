#Used by: Item: Hardwiring - 'Snapshot' ZMTX
from customEffects import boostAmmoListBySkillReq
def missileExplosiveDmgBonusTorpedo(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Torpedoes", self.item)