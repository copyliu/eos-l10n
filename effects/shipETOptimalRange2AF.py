#Item: Imperial Navy Slicer
from customEffects import boostModListBySkillReq
def shipETOptimalRange2AF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonus2AF",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)
