#Item: Legion Propulsion - Fuel Catalyst
from customEffects import boostModListBySkillReq
def subsystemBonusAmarrPropulsionAfterburnerSpeedFactor(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Propulsion Systems")
    boostModListBySkillReq(fitting.modules, "speedFactor", "subsystemBonusAmarrPropulsion",
                           lambda skill: skill.name == "Afterburner",
                           self.item, extraMult = level)