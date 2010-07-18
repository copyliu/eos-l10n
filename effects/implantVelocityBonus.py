#Items from group: Cyber Navigation (4 of 27) [Implant]
from customEffects import boost
def implantVelocityBonus(self, fitting):
    boost(fitting.ship, "maxVelocity", "implantBonusVelocity", self.item)