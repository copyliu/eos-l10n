#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Industry Implants (3 of 9)
#Item: Mining Upgrades [Skill]
from customEffects import boostModListBySkillReq
def miningUpgradeCPUPenaltyReductionModulesRequiringMiningUpgradePercent(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "cpuPenaltyPercent", "miningUpgradeCPUReductionBonus",
                           lambda skill: skill.name == "Mining Upgrades",
                           self.item, extraMult = level)