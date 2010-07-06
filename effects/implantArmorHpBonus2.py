#Used by: Item: Hardwiring 'Noble' ZET5X
from customEffects import boost
def implantArmorHpBonus2(self, fitting):
    boost(fitting.ship, "armorHP", "armorHpBonus2", self.item)