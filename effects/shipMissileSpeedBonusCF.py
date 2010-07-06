#Used by: Ship: Buzzard
from customEffects import boostModListBySkillReq
def shipMissileSpeedBonusCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusCF",
                           lambda skill: skill.name == "Missile Launcher Operation",
                           self.item, extraMult = level)