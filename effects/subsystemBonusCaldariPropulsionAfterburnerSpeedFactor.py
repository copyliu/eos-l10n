#Item: Tengu Propulsion - Fuel Catalyst [Subsystem]
from customEffects import boostModListBySkillReq
def subsystemBonusCaldariPropulsionAfterburnerSpeedFactor(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Propulsion Systems")
    boostModListBySkillReq(fitting.modules, "speedFactor", "subsystemBonusCaldariPropulsion",
                           lambda skill: skill.name == "Afterburner",
                           self.item, extraMult = level)