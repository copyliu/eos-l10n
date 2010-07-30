#Items with name like: Low Friction Nozzle Joints (6 of 6)
#Items with name like: Low-grade Nomad (5 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Navigation Implants (3 of 4)
#Item: Evasive Maneuvering [Skill]
#Item: Spaceship Command [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("agility", container.getModifiedItemAttr("agilityBonus") * level,
                           stackingPenalties = "skill" not in context and "implant" not in context)
