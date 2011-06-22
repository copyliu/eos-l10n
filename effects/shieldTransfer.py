# Used by:
# Modules from group: Shield Transporter (39 of 39)
# Drones named like: Shield Maintenance Bot (6 of 6)
type = "projected", "active"
def handler(fit, container, context):
    if "projected" in context and not fit.ship.getModifiedItemAttr("disallowAssistance") == 1:
        bonus = container.getModifiedItemAttr("shieldBonus")
        duration = container.getModifiedItemAttr("duration") / 1000.0
        fit.extraAttributes.increase("shieldRepair", bonus / duration)
