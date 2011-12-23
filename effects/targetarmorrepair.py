# Used by:
# Modules from group: Armor Repair Projector (39 of 39)
# Drones named like: Armor Maintenance Bot (6 of 6)
type = "projected", "active"
def handler(fit, container, context):
    if "projected" in context:
        bonus = container.getModifiedItemAttr("armorDamageAmount")
        duration = container.getModifiedItemAttr("duration") / 1000.0
        fit.extraAttributes.increase("armorRepair", bonus / duration)
