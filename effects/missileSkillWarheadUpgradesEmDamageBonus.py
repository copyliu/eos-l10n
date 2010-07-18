#Item: Warhead Upgrades
from customEffects import boostAmmoListBySkillReq
def missileSkillWarheadUpgradesEmDamageBonus(self, fitting, level):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)