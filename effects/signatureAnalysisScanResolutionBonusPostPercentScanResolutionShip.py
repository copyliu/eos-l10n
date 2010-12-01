#Used by:
#Implants named like: Hardwiring Zainou 'Gypsy' KNB (3 of 3)
#Skill: Signature Analysis
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("scanResolution", container.getModifiedItemAttr("scanResolutionBonus") * level)
