#Item: Warhead Upgrades [Skill]
from customEffects import boostAmmoListBySkillReq
def missileSkillWarheadUpgradesExplosiveDamageBonus(self, fitting, level):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)