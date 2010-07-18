#Items from market group: Ammunition & Charges > Missiles > Cruise Missiles > Advanced High Damage Cruise Missiles (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Heavy Assault Missiles > Advanced Anti-Ship Assault Missile (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Heavy Missiles > Advanced High Damage Heavy Missiles (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Light Missiles > Advanced High Damage Light Missiles (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Rockets > Advanced Anti-Ship Rockets (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Torpedoes > Advanced Anti-Ship Torpedoes (4 of 4)
from customEffects import boost
def increaseSignatureRadiusPassive(self, fitting, containerModule):
    boost(fitting.ship, "signatureRadius", "signatureRadiusBonus", self.item)
