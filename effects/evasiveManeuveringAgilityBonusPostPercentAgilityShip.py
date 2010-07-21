#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Navigation Implants (3 of 4)
#Variations of item: Large Low Friction Nozzle Joints I (2 of 2) [Module]
#Variations of item: Medium Low Friction Nozzle Joints I (2 of 2) [Module]
#Variations of item: Small Low Friction Nozzle Joints I (2 of 2) [Module]
#Item: Evasive Maneuvering [Skill]
#Item: Low-grade Nomad Alpha [Implant]
#Item: Low-grade Nomad Beta [Implant]
#Item: Low-grade Nomad Delta [Implant]
#Item: Low-grade Nomad Epsilon [Implant]
#Item: Low-grade Nomad Gamma [Implant]
#Item: Spaceship Command [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.ship.boostItemAttr("agility", container.getModifiedItemAttr("agilityBonus") * level,
                           stackingPenalties = context != "skill" and context != "implant")