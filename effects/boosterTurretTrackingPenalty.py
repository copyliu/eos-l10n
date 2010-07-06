#Used by: Item: Frentix Booster
#               Exile Booster
type = "boosterSideEffect"
from customEffects import boostModListBySkillReq
def boosterTurretTrackingPenalty(self, fitting):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "boosterTurretTrackingPenalty",
                           lambda skill: skill.name == "Gunnery", self.item)