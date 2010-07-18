#Variations of item: Brutix (3 of 3)
from customEffects import boostModListBySkillReq
def shipHybridDmgGBC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusBC1",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)