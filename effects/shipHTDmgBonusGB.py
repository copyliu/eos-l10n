#Items from category: Ship (8 of 245)
from customEffects import boostModListBySkillReq
def shipHTDmgBonusGB(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusGB",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item, extraMult = level)
