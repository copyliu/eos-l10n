#Used by:
#Implants named like: Snake (11 of 12)
#Modules named like: Auxiliary Thrusters (6 of 6)
#Skill: Navigation
type = "passive"
def handler(fit, container, context):
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("velocityBonus"),
                           stackingPenalties = "skill" not in context and "implant" not in context)
