#Item: Hardwiring - Eifyr and Co. 'Gunslinger' AX-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' AX-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' AX-2 [Implant]
#Item: Motion Prediction [Skill]
#Item: Ogdin's Eye Coordination Enhancer [Implant]
from customEffects import boostModListBySkillReq
def trackingSpeedBonusPassiveRequiringGunneryTrackingSpeedBonus(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)