#Used by: Item : Focusing Kit
#         Skill: Survey
from customEffects import boostModListBySkillReq
def surveyScanspeedBonusPostPercentDurationLocationShipModulesRequiringElectronics(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "duration", "scanspeedBonus",
                           lambda skill: skill.name == "Electronics",
                           self.item, extraMult = level)