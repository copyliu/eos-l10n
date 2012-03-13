# Used by:
# Implants named like: Zainou 'Gypsy' Signature Analysis SA (6 of 6)
# Implant: Quafe Zero
# Skill: Signature Analysis
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("scanResolution", container.getModifiedItemAttr("scanResolutionBonus") * level)
