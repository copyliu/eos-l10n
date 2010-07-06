#Used by: Item: Proteus Offensive - Dissonic Encoding Platform
from customEffects import boostModListBySkillReq
def subsystemBonusGallenteOffensiveHybridWeaponFalloff(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Offensive Systems")
    boostModListBySkillReq(fitting.modules, "falloff", "subsystemBonusGallenteOffensive",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)