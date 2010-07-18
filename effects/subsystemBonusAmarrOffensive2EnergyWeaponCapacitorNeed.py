#Item: Legion Offensive - Drone Synthesis Projector [Subsystem]
#Item: Legion Offensive - Liquid Crystal Magnifiers [Subsystem]
from customEffects import boostModListBySkillReq
def subsystemBonusAmarrOffensive2EnergyWeaponCapacitorNeed(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "subsystemBonusAmarrOffensive2",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)