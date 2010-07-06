#Used by: Ship: Vulture
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipHybridOptimalCS1(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "maxRange", "eliteBonusCommandShips1",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)