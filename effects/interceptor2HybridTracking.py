#Used by: Ship: Taranis
from customEffects import boostModListBySkillReq
def interceptor2HybridTracking(self, fitting):
    skill, level = fitting.getCharSkill("Interceptors")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "eliteBonusInterceptor2",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)