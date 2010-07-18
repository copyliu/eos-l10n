#Item: Sin
from customEffects import boost
def eliteBonusBlackOpsAgiliy1(self, fitting):
    skill, level = fitting.getCharSkill("Black Ops")
    boost(fitting.ship, "agility", "eliteBonusBlackOps1",
          self.item, extraMult = level)