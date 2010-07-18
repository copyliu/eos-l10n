from customEffects import boost
def shipVelocityBonusATC1(self, fitting):
    boost(fitting.ship, "maxVelocity", "shipBonusATC1", self.item)