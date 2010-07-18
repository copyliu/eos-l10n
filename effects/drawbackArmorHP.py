#Items from group: Rig Astronautic (48 of 48)
from customEffects import boost
def drawbackArmorHP(self, fitting, state):
    boost(fitting.ship, "armorHP", "drawback", self.item)