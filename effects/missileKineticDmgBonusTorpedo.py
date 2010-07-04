#Used by: Item: Hardwiring - 'Snapshot' ZMTX
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusTorpedo(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Torpedoes", self.item)