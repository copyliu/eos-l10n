#Used by: Ship: Dramiel
from customEffects import boostModListBySkillReq
def shipFalloffBonusMF(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusMF",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)