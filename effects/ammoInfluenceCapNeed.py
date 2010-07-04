#Used by: All ammo
from customEffects import boost
def ammoInfluenceCapNeed(self, fitting, containerModule):
    boost(containerModule, "capacitorNeed", "capNeedBonus", self.item)