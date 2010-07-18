#Items from group: Advanced Cruise Missile (4 of 8) [Charge]
#Items from group: Advanced Heavy Missile (4 of 8) [Charge]
#Items from group: Advanced Light Missile (4 of 8) [Charge]
#Items from group: Advanced Torpedo (4 of 8) [Charge]
#Items from market group: Ammunition & Charges > Missiles > Heavy Assault Missiles > Advanced Anti-Ship Assault Missile (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Rockets > Advanced Anti-Ship Rockets (4 of 4)
from customEffects import boost
def increaseSignatureRadiusPassive(self, fitting, containerModule):
    boost(fitting.ship, "signatureRadius", "signatureRadiusBonus", self.item)
