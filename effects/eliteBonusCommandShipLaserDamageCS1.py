#Used by: Ship: Absolution
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipLaserDamageCS1(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusCoverOps1",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)