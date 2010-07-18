#Item: Astarte [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipHybridDamageCS1(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusCommandShips1",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)