#Item: Proteus Offensive - Covert Reconfiguration
from customEffects import boostModListBySkillReq
def subsystemBonusGallenteOffensiveHybridWeaponDamageMultiplier(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Offensive Systems")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "subsystemBonusGallenteOffensive",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)