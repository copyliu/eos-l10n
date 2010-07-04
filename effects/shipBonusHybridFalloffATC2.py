#Used by: Ship: Adrestia
from customEffects import boostModListBySkillReq
def shipBonusHybridFalloffATC2(self, fitting):
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusATC2",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item)