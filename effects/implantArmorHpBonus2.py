#Used by:
#Implant: Akemon's Modified 'Noble' ZET5000
#Implant: Hardwiring - Inherent Implants 'Noble' ZET50
#Implant: Hardwiring - Inherent Implants 'Noble' ZET500
#Implant: Hardwiring - Inherent Implants 'Noble' ZET5000
#Implant: Imperial Navy Modified 'Noble' Implant
#Implant: Imperial Special Ops Field Enhancer - Standard
type = "passive"
def handler(fit, implant, context):
    fit.ship.boostItemAttr("armorHP", implant.getModifiedItemAttr("armorHpBonus2"))