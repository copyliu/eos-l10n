#Used by:
#Implant: Hardwiring - Inherent Implants 'Noble' ZET30
#Implant: Hardwiring - Inherent Implants 'Noble' ZET300
#Implant: Hardwiring - Inherent Implants 'Noble' ZET3000
#Skill: Mechanic
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("hp", container.getModifiedItemAttr("hullHpBonus") * level)
