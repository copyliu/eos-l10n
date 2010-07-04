#Used by: Item: Drop Booster
from customEffects import boostModListBySkillReq
def motionPredictionTrackingSpeedMultiplierPostPercentTrackingSpeedLocationShipModulesRequiringGunnery(self, fitting):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedMultiplier",
                           lambda skill: skill.name == "Gunnery", self.item)