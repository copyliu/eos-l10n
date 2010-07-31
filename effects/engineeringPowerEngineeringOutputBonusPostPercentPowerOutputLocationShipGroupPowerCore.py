#Used by:
#Implants named like: Hardwiring Inherent Implants 'Squire' PG (3 of 3)
#Modules named like: Ancillary Current Router (6 of 6)
#Skill: Engineering
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("powerOutput", container.getModifiedItemAttr("powerEngineeringOutputBonus") * level)
