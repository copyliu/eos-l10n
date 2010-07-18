#Variations of item: Megathron (3 of 5)
from customEffects import boostModListBySkillReq
def shipHTTrackingBonusGB2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusGB2",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item, extraMult = level)
