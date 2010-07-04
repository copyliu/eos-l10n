#Used by: Item: Loki Propulsion - Fuel Catalyst
from customEffects import boostModListBySkillReq
def subsystemBonusMinmatarPropulsionAfterburnerSpeedFactor(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Propulsion Systems")
    boostModListBySkillReq(fitting.modules, "speedFactor", "subsystemBonusMinmatarPropulsion",
                           lambda skill: skill.name == "Afterburner",
                           self.item, extraMult = level)