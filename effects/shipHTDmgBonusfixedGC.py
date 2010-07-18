#Items from category: Ship (11 of 245)
from customEffects import boostModListBySkillReq
def shipHTDmgBonusfixedGC(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusGC",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)
