#Items from group: Interceptor (8 of 8) [Ship]
from customEffects import boostModListBySkillReq
def interceptorMWDSignatureRadiusBonus(self, fitting):
    skill, level = fitting.getCharSkill("Interceptors")
    boostModListBySkillReq(fitting.modules, "signatureRadiusBonus", "eliteBonusInterceptor",
                           lambda skill: skill.name == "High Speed Maneuvering",
                           self.item, extraMult = level)