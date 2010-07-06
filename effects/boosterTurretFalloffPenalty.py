#Used by: Item: Drop Booster
#               X-Instinct Booster
type = "boosterSideEffect"
from customEffects import boostModListBySkillReq
def boosterTurretFalloffPenalty(self, fitting):
    boostModListBySkillReq(fitting.modules, "falloff", "boosterTurretFalloffPenalty",
                           lambda skill: skill.name == "Gunnery", self.item)