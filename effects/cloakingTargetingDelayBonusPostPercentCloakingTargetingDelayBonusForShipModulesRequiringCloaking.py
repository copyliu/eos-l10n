#Item: Cloaking
from customEffects import boostModListBySkillReq
def cloakingTargetingDelayBonusPostPercentCloakingTargetingDelayBonusForShipModulesRequiringCloaking(self, fitting, level):
    boostModListBySkillReq(fitting.modules, "cloakingTargetingDelay", "cloakingTargetingDelayBonus",
                           lambda skill: skill.name == "Cloaking", self.item, extraMult = level)
