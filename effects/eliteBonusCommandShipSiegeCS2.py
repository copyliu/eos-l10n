#Item: Vulture [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipSiegeCS2(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "commandBonus", "eliteBonusCommandShips2",
                           lambda skill: skill.name == "Siege Warfare Specialist",
                           self.item, extraMult = level)