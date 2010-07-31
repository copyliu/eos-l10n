#Used by:
#Implants named like: Hardwiring Zainou 'Gypsy' KPB (3 of 3)
#Skill: Long Range Targeting
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("maxTargetRangeBonus") * level)
