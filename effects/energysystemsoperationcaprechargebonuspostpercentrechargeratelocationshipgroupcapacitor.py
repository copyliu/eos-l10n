# Used by:
# Implants named like: Hardwiring Inherent Implants 'Squire' CR (6 of 6)
# Modules named like: Capacitor Control Circuit (6 of 6)
# Skill: Energy Systems Operation
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("rechargeRate", container.getModifiedItemAttr("capRechargeBonus") * level)
