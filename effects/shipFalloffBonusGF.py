#Items from group: Frigate (3 of 35)
from customEffects import boostModListBySkillReq
def shipFalloffBonusGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusGF2",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)