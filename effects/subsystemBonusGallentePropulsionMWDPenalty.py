#Item: Proteus Propulsion - Wake Limiter
from customEffects import boostModListBySkillReq
def subsystemBonusGallentePropulsionMWDPenalty(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Propulsion Systems")
    boostModListBySkillReq(fitting.modules, "signatureRadiusBonus", "subsystemBonusGallentePropulsion",
                           lambda skill: skill.name == "High Speed Maneuvering",
                           self.item, extraMult = level)