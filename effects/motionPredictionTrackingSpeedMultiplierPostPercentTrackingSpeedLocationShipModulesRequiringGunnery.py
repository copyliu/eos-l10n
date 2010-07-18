#Item: Improved Drop Booster [Implant]
#Item: Standard Drop Booster [Implant]
#Item: Strong Drop Booster [Implant]
#Item: Synth Drop Booster [Implant]
from customEffects import boostModListBySkillReq
def motionPredictionTrackingSpeedMultiplierPostPercentTrackingSpeedLocationShipModulesRequiringGunnery(self, fitting):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedMultiplier",
                           lambda skill: skill.name == "Gunnery", self.item)