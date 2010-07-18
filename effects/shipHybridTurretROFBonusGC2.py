#Item: Exequror Navy Issue
from customEffects import boostModListBySkillReq
def shipHybridTurretROFBonusGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusGC2",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)
