#Used by: Ship: Dominix
#               Dominix Navy Issue
#               Megathron
#               Megathron Navy Issue
#               Megathron Federate Issue
#               Hyperion
#               Sin
#               Kronos
from customEffects import boostModListBySkillReq
def shipHTDmgBonusGB(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusGB",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item, extraMult = level)
