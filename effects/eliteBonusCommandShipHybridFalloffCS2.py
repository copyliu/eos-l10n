#Item: Astarte
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipHybridFalloffCS2(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "maxRange", "eliteBonusCommandShips2",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)