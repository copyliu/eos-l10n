#Used by:
#Modules from group: Shield Transporter (38 of 38)
#Drones named like: Shield Maintenance Bot (6 of 6)
type = "projected", "active"
def handler(fit, container, context):
    if "projected" not in context: return
    bonus = container.getModifiedItemAttr("shieldBonus")
    duration = container.getModifiedItemAttr("duration")
    fit.extraAttributes["shieldRepair"].increase(bonus / duration)
