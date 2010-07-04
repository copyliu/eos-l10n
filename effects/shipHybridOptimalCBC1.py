#Used by: Ship: Ferox
#               Vulture
from customEffects import boostModListBySkillReq
def shipHybridOptimalCBC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusBC1",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           extraMult = level)