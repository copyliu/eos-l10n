#Item: Legion Offensive - Liquid Crystal Magnifiers
from customEffects import boostModListBySkillReq
def subsystemBonusAmarrOffensiveEnergyWeaponDamageMultiplier(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "subsystemBonusAmarrOffensive",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)