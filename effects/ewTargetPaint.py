#Items from group: Target Painter (9 of 9) [Module]
#Item: Berserker TP-900 [Drone]
#Item: Valkyrie TP-600 [Drone]
#Item: Warrior TP-300 [Drone]
type = "projected", "active"
def handler(fit, container, context):
    if "projected" in context:
        fit.ship.boostItemAttr("signatureRadius", container.getModifiedItemAttr("signatureRadiusBonus"),
                               stackingPenalties = True)
