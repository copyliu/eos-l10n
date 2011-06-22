# Used by:
# Implants named like: Hardwiring Eifyr and Co. 'Rogue' AY (6 of 6)
# Implants named like: Low grade Nomad (5 of 6)
# Modules named like: Low Friction Nozzle Joints (6 of 6)
# Skill: Evasive Maneuvering
# Skill: Spaceship Command
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("agility", container.getModifiedItemAttr("agilityBonus") * level,
                           stackingPenalties = "skill" not in context and "implant" not in context)
