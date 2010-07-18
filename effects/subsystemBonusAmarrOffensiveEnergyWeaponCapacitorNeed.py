#Item: Legion Offensive - Covert Reconfiguration [Subsystem]
from customEffects import boostModListBySkillReq
def subsystemBonusAmarrOffensiveEnergyWeaponCapacitorNeed(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "subsystemBonusAmarrOffensive",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)