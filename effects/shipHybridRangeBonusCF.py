#Used by: Ship: Ibis
#               Harpy
from customEffects import boostModListBySkillReq
def shipHybridRangeBonusCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusCF",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)