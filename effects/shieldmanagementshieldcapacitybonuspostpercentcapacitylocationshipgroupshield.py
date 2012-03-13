# Used by:
# Implants named like: Zainou 'Gnome' Shield Management SM (6 of 6)
# Modules named like: Core Defense Field Extender (6 of 6)
# Modules named like: QA Multiship Module Players (4 of 4)
# Implant: Sansha Modified 'Gnome' Implant
# Skill: Shield Management
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("shieldCapacity", container.getModifiedItemAttr("shieldCapacityBonus") * level)
