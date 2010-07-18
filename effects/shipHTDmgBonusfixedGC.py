#Variations of item: Celestis (3 of 3) [Ship]
#Variations of item: Thorax (3 of 4) [Ship]
#Variations of item: Vexor (4 of 4) [Ship]
#Item: Exequror Navy Issue [Ship]
from customEffects import boostModListBySkillReq
def shipHTDmgBonusfixedGC(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusGC",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)
