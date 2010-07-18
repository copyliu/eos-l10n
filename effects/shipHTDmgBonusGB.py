#Variations of item: Dominix (3 of 3) [Ship]
#Variations of item: Megathron (4 of 5) [Ship]
#Item: Hyperion [Ship]
from customEffects import boostModListBySkillReq
def shipHTDmgBonusGB(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusGB",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item, extraMult = level)
