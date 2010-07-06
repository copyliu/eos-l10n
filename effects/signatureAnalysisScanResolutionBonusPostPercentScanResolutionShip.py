#Used by: Skill: Signature Analysis
from customEffects import boost
def signatureAnalysisScanResolutionBonusPostPercentScanResolutionShip(self, fitting, level = 1):
    boost(fitting.ship, "scanResolution", "scanResolutionBonus",
          self.item, extraMult = level)