#Used by: Ship: Dramiel
from customEffects import boostModListBySkillReq
def shipBonusPirateFrigateProjDamage(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusPirateFaction",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item)