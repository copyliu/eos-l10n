#Used by: Skill: Warhead Upgrades
from customEffects import boostAmmoListBySkillReq
def missileSkillWarheadUpgradesThermalDamageBonus(self, fitting, level):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)