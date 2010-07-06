#Used by: Item: All astrometrics rigs
from customEffects import boost
def drawbackArmorHP(self, fitting, state):
    boost(fitting.ship, "armorHP", "drawback", self.item)