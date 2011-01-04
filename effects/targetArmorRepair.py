#Used by:
#Modules from group: Armor Repair Projector (38 of 38)
#Drones named like: Armor Maintenance Bot (6 of 6)
type = "projected", "active"
def handler(fit, container, context):
    if "projected" in context and not fit.ship.getModifiedItemAttr("disallowAssistance") == 1:
        bonus = container.getModifiedItemAttr("armorDamageAmount")
        duration = container.getModifiedItemAttr("duration") / 1000.0
        fit.extraAttributes.increase("armorRepair", bonus / duration)
