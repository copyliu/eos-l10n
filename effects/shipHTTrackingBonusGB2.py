#Used by: Ship: Megathron
#               Megathron Navy Issue
#               Megathron Federate Issue
from customEffects import boostModListBySkillReq
def shipHTTrackingBonusGB2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusGB2",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item, extraMult = level)
