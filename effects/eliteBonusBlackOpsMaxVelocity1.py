#Item: Panther [Ship]
from customEffects import boost
def eliteBonusBlackOpsMaxVelocity1(self, fitting):
    skill, level = fitting.getCharSkill("Black Ops")
    boost(fitting.ship, "maxVelocity", "eliteBonusBlackOps1",
          self.item, extraMult = level)