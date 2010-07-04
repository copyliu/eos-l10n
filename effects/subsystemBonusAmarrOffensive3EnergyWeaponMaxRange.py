#Used by: Item: Legion Offensive - Liquid Crystal Magnifiers
from customEffects import boostModListBySkillReq
def subsystemBonusAmarrOffensive3EnergyWeaponMaxRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostModListBySkillReq(fitting.modules, "maxRange", "subsystemBonusAmarrOffensive3",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)