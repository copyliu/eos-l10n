#Used by: Item: Proteus Offensive - Dissonic Encoding Platform
from customEffects import boostModListBySkillReq
def subsystemBonusGallenteOffensive3TurretTracking(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Offensive Systems")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "subsystemBonusGallenteOffensive3",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)