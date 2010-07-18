#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Electronics Implants (3 of 3)
#Item: Signature Analysis [Skill]
from customEffects import boost
def signatureAnalysisScanResolutionBonusPostPercentScanResolutionShip(self, fitting, level = 1):
    boost(fitting.ship, "scanResolution", "scanResolutionBonus",
          self.item, extraMult = level)