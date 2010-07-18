#Items from market group: Implants & Boosters > Booster (4 of 32)
from customEffects import boostModListBySkillReq
def motionPredictionTrackingSpeedMultiplierPostPercentTrackingSpeedLocationShipModulesRequiringGunnery(self, fitting):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedMultiplier",
                           lambda skill: skill.name == "Gunnery", self.item)