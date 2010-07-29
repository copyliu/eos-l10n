#Items from group: Armor Repair Projector (37 of 37) [Module]
#Items from group: Logistic Drone (6 of 12) [Drone]
type = "projected", "active"
def handler(fit, container, context):
    if "projected" not in context or fit.ship.getModifiedItemAttr("disallowAssistance") == 1:
        return
    amount = container.getModifiedItemAttr("armorDamageAmount")
    speed = container.getModifiedAttribute("duration") / 1000.0
    fit.extraAttributes["armorRepair"].increase(amount / speed)
