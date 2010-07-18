#Items from group: Interceptor (8 of 8)
from customEffects import boostModListBySkillReq
def shipCapPropulsionJamming(self, fitting):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "eliteBonusInterceptorRole",
                           lambda skill: skill.name == "Propulsion Jamming", self.item)