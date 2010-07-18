#Item: Falcon
from customEffects import boostModListBySkillReq
def shipBonusMediumHybridDmgCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusCC2",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)