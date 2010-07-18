#Item: Hardwiring - Inherent Implants 'Highwall' HY-0 [Implant]
#Item: Hardwiring - Inherent Implants 'Highwall' HY-1 [Implant]
#Item: Hardwiring - Inherent Implants 'Highwall' HY-2 [Implant]
#Item: Mining Upgrades [Skill]
from customEffects import boostModListBySkillReq
def miningUpgradeCPUPenaltyReductionModulesRequiringMiningUpgradePercent(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "cpuPenaltyPercent", "miningUpgradeCPUReductionBonus",
                           lambda skill: skill.name == "Mining Upgrades",
                           self.item, extraMult = level)