#Items from group: Logistic Drone (6 of 12) [Drone]
#Items from group: Shield Transporter (38 of 38) [Module]
type = "projected", "active"
def handler(fit, container, context):
    if context != "projected": return
    bonus = container.getModifiedItemAttr("shieldBonus")
    duration = container.getModifiedItemAttr("duration")
    fit.ship.shieldRepair += bonus / duration