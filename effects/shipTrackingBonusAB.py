#Item: Nightmare
from customEffects import boostModListBySkillReq
def shipTrackingBonusAB(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusAB2",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item, extraMult = level)