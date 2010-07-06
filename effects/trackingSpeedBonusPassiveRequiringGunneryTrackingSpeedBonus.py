#Used by: Skill: Motion Prediction
from customEffects import boostModListBySkillReq
def trackingSpeedBonusPassiveRequiringGunneryTrackingSpeedBonus(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)