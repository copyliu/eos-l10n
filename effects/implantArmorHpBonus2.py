#Used by:
#Implants named like: Modified 'Noble' (2 of 2)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Armor Implants (3 of 3)
#Implant: Imperial Special Ops Field Enhancer - Standard
type = "passive"
def handler(fit, implant, context):
    fit.ship.boostItemAttr("armorHP", implant.getModifiedItemAttr("armorHpBonus2"))