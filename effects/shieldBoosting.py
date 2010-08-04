#Used by:
#Modules from group: Shield Booster (86 of 86)
runTime = "late"
type = "active"
def handler(fit, module, context):
    amount = module.getModifiedItemAttr("shieldBonus")
    speed = module.getModifiedItemAttr("duration") / 1000.0
    fit.extraAttributes.increase("shieldRepair", amount / speed)