#Items from group: Cyberimplant (11 of 138) [Implant]
#Variations of item: Large Auxiliary Thrusters I (2 of 2) [Module]
#Variations of item: Medium Auxiliary Thrusters I (2 of 2) [Module]
#Variations of item: Small Auxiliary Thrusters I (2 of 2) [Module]
#Item: Navigation [Skill]
type = "passive"
def handler(fit, container, context):
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("velocityBonus"),
                           stackingPenalties = context != "skill" and context != "implant")