#Used by: Item: Hardwiring - 'Snapshot' ZMUX
from customEffects import boostAmmoListBySkillReq
def missileExplosiveDmgBonusCruise3(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Cruise Missiles", self.item)