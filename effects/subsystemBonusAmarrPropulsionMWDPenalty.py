#Item: Legion Propulsion - Wake Limiter [Subsystem]
from customEffects import boostModListBySkillReq
def subsystemBonusAmarrPropulsionMWDPenalty(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Propulsion Systems")
    boostModListBySkillReq(fitting.modules, "signatureRadiusBonus", "subsystemBonusAmarrPropulsion",
                           lambda skill: skill.name == "High Speed Maneuvering",
                           self.item, extraMult = level)