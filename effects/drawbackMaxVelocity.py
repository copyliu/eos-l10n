#Used by: Item: Anti-EM Pump 
#               Anti-Explosive Pump
#               Anti-Kinetic Pump
#               Anti-Thermic Pump
#               Auxiliary Nano Pump
#               Nanobot Accelerator
#               Trimark Armor Pump
from customEffects import boost
def drawbackMaxVelocity(self, fitting, state):
    boost(fitting.ship, "maxVelocity", "drawback", self.item, useStackingPenalty = True)