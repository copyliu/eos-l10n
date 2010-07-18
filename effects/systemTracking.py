#Items from group: Effect Beacon (6 of 38)
from customEffects import boostModListBySkillReq, multiply
type = "projected"
def systemTracking(self, fitting, state):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedMultiplier",
                      lambda skill: skill.name == "Gunnery",
                      self.item, helper = multiply)