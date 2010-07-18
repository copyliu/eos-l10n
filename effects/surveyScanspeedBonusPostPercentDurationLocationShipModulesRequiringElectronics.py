#Variations of item: Large Signal Focusing Kit I (2 of 2) [Module]
#Variations of item: Medium Signal Focusing Kit I (2 of 2) [Module]
#Variations of item: Small Signal Focusing Kit I (2 of 2) [Module]
#Item: Survey [Skill]
from customEffects import boostModListBySkillReq
def surveyScanspeedBonusPostPercentDurationLocationShipModulesRequiringElectronics(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "duration", "scanspeedBonus",
                           lambda skill: skill.name == "Electronics",
                           self.item, extraMult = level)