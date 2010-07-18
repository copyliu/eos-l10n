#Variations of item: Moa (2 of 4) [Ship]
from customEffects import boostModListBySkillReq
def shipHRangeBonusCC(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusCC",
                      lambda skill: skill.name == "Medium Hybrid Turret",
                      self.item, extraMult = level)