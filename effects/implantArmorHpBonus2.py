#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Armor Implants (3 of 3)
#Item: Akemon's Modified 'Noble' ZET5000 [Implant]
#Item: Imperial Navy Modified 'Noble' Implant [Implant]
#Item: Imperial Special Ops Field Enhancer - Standard [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.ship.boostItemAttr("armorHP", implant.getModifiedItemAttr("armorHpBonus2"))