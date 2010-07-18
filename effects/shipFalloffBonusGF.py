#Item: Atron [Ship]
#Item: Daredevil [Ship]
#Item: Incursus [Ship]
from customEffects import boostModListBySkillReq
def shipFalloffBonusGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusGF2",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)