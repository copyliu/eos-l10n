#Used by: Item: Hardwiring - 'Snapshot' ZMHX
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusHeavy(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Missiles", self.item)