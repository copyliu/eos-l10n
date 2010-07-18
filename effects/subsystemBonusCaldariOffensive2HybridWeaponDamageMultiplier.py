#Item: Tengu Offensive - Magnetic Infusion Basin
from customEffects import boostModListBySkillReq
def subsystemBonusCaldariOffensive2HybridWeaponDamageMultiplier(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Offensive Systems")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "subsystemBonusCaldariOffensive2",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)