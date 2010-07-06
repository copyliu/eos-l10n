#Used by: Ship: Prowler
#               Mastodon
from customEffects import boost
def shipVelocityBonusMI(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Industrial")
    boost(fitting.ship, "maxVelocity", "shipBonusMI", self.item,
          extraMult = level)