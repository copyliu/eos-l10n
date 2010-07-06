#Used by: Item: Tengu Offensive - Magnetic Infusion Basin
from customEffects import boostModListBySkillReq
def subsystemBonusCaldariOffensiveHybridWeaponMaxRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Offensive Systems")
    boostModListBySkillReq(fitting.modules, "maxRange", "subsystemBonusCaldariOffensive",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)