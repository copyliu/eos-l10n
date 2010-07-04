#Used by: Ship: Crusader
from customEffects import boostModListBySkillReq
def interceptor2LaserTracking(self, fitting):
    skill, level = fitting.getCharSkill("Interceptors")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "eliteBonusInterceptor2",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)