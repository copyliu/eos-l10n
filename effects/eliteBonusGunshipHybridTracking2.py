#Used by: Ship: Enyo
from customEffects import boostModListBySkillReq
def eliteBonusGunshipHybridTracking2(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "eliteBonusGunship2",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)