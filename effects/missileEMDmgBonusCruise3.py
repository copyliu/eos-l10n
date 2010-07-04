#Used by: Item: Hardwiring - 'Snapshot' ZMUX
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusCruise3(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Cruise Missiles", self.item)