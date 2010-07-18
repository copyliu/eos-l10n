#Item: Absolution
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipLaserROFCS2(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "speed", "eliteBonusCommandShips2",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)