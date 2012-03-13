# Used by:
# Implants named like: Inherent Implants 'Squire' Engineering EG (6 of 6)
# Modules named like: Ancillary Current Router (6 of 6)
# Implant: Genolution Core Augmentation CA-1
# Skill: Engineering
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("powerOutput", container.getModifiedItemAttr("powerEngineeringOutputBonus") * level)
