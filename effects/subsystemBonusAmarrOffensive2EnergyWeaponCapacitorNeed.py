#Used by: Item: Legion Offensive - Drone Synthesis Projector
#               Legion Offensive - Liquid Crystal Magnifiers
from customEffects import boostModListBySkillReq
def subsystemBonusAmarrOffensive2EnergyWeaponCapacitorNeed(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "subsystemBonusAmarrOffensive2",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)