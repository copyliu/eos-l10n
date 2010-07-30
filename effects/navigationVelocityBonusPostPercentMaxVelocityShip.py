#Items with name like: Auxiliary Thrusters (6 of 6)
#Items with name like: Snake (11 of 13)
#Item: Navigation [Skill]
type = "passive"
def handler(fit, container, context):
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("velocityBonus"),
                           stackingPenalties = "skill" not in context and "implant" not in context)
