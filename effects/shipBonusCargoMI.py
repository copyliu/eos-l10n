#Used by: Ship: Prowler
#               Mastodon
from customEffects import boost
def shipBonusCargoMI(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Industrial")
    boost(fitting.ship, "capacity", "shipBonusMI", self.item,
          extraMult = level)