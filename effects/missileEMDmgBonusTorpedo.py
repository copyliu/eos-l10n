#Used by: Item: Hardwiring - 'Snapshot' ZMTX
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusTorpedo(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Torpedoes", self.item)