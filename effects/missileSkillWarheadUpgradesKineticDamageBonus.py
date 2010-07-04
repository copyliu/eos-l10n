#Used by: Skill: Warhead Upgrades
from customEffects import boostAmmoListBySkillReq
def missileSkillWarheadUpgradesKineticDamageBonus(self, fitting, level):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)