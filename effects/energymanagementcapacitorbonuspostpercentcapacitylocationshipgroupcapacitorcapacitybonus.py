# Used by:
# Implants named like: Inherent Implants 'Squire' Energy Management EM (6 of 6)
# Implants named like: Mindflood Booster (4 of 4)
# Modules named like: Semiconductor Memory Cell (6 of 6)
# Implant: Genolution Core Augmentation CA-1
# Skill: Energy Management
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("capacitorCapacity", container.getModifiedItemAttr("capacitorCapacityBonus") * level)
