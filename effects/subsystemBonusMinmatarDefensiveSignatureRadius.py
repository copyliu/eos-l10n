#Item: Loki Defensive - Amplification Node
from customEffects import boost
def subsystemBonusMinmatarDefensiveSignatureRadius(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Defensive Systems")
    boost(fitting.ship, "signatureRadius", "subsystemBonusMinmatarDefensive",
          self.item, extraMult = level)