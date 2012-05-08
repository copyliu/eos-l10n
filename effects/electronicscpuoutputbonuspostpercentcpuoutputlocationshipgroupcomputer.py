# Used by:
# Implants named like: Zainou 'Gypsy' Electronics EE (6 of 6)
# Modules named like: Processor Overclocking Unit (6 of 6)
# Implant: Genolution Core Augmentation CA-2
# Skill: Electronics
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("cpuOutput", container.getModifiedItemAttr("cpuOutputBonus2") * level)
