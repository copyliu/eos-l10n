#Used by: Item: Magnatar Effect Beacon
from customEffects import boostModListBySkillReq, multiply
type = "projected"
def systemTracking(self, fitting, state):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedMultiplier",
                      lambda skill: skill.name == "Gunnery",
                      self.item, helper = multiply)