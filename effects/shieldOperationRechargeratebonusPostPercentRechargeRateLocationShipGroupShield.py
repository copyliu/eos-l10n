#Used by:
#Implants named like: Hardwiring Zainou 'Gnome' KYA (6 of 6)
#Modules named like: Core Defence Field Purger (6 of 6)
#Implant: Sansha Modified 'Gnome' Implant
#Skill: Shield Operation
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("shieldRechargeRate", container.getModifiedItemAttr("rechargeratebonus") * level)
