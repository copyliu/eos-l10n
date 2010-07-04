#Used by: Item: Hardwiring - 'Snapshot' ZMUX
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusCruise3(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Cruise Missiles", self.item)