# Used by:
# Implants named like: Hardwiring Zainou 'Gypsy' KMB (6 of 6)
# Implant: Hardwiring - Genolution Core Augmentation CA-2
# Skill: Electronics
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("cpuOutput", container.getModifiedItemAttr("cpuOutputBonus2") * level)
