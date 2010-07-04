#Used by: Item: Hardwiring - 'Snapshot' ZMHX
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusHeavy(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Missiles", self.item)