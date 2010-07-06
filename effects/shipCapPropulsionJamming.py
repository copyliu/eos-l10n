#Used by: Ship: Crow
#               Raptor
#               Crusader
#               Malediction
#               Claw
#               Stilleto
#               Taranis
#               Ares
from customEffects import boostModListBySkillReq
def shipCapPropulsionJamming(self, fitting):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "eliteBonusInterceptorRole",
                           lambda skill: skill.name == "Propulsion Jamming", self.item)