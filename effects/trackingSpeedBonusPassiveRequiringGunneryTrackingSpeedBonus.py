#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Gunnery Implants (3 of 9)
#Item: Motion Prediction [Skill]
#Item: Ogdin's Eye Coordination Enhancer [Implant]
from customEffects import boostModListBySkillReq
def trackingSpeedBonusPassiveRequiringGunneryTrackingSpeedBonus(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)