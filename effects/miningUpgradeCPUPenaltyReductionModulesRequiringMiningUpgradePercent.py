#Used by: Skill: Mining Upgrades
#         Item : Hardwiring - 'Highwall' HY-X
from customEffects import boostModListBySkillReq
def miningUpgradeCPUPenaltyReductionModulesRequiringMiningUpgradePercent(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "cpuPenaltyPercent", "miningUpgradeCPUReductionBonus",
                           lambda skill: skill.name == "Mining Upgrades",
                           self.item, extraMult = level)