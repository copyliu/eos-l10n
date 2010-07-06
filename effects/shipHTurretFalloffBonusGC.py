#Used by: Ship: Vigilant
from customEffects import boostModListBySkillReq
def shipHTurretFalloffBonusGC(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusGC",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)