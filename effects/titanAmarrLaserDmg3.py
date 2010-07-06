#Used by: Ship: Avatar
from customEffects import boostModListBySkillReq
def titanAmarrLaserDmg3(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Titan")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "titanAmarrBonus3",
                           lambda skill: skill.name == "Capital Energy Turret",
                           self.item, extraMult = level)