#Used by:
#Implants named like: Snake (11 of 12)
#Modules named like: Auxiliary Thrusters (6 of 6)
#Skill: Navigation
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("velocityBonus") * level,
                           stackingPenalties = "skill" not in context and "implant" not in context)
