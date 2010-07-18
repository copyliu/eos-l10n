#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Armor Implants (3 of 3)
#Item: Akemon's Modified 'Noble' ZET5000
#Item: Imperial Navy Modified 'Noble' Implant
#Item: Imperial Special Ops Field Enhancer - Standard
from customEffects import boost
def implantArmorHpBonus2(self, fitting):
    boost(fitting.ship, "armorHP", "armorHpBonus2", self.item)