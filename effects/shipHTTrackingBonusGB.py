#Used by: Ship: Vindicator
from customEffects import boostModListBySkillReq
def shipHTTrackingBonusGB(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusGB",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item, extraMult = level)