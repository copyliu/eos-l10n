#Used by:
#Subsystems from group: Defensive Systems (16 of 16)
type = "passive"
def handler(fit, module, context):
    fit.extraAttributes.increase("capacity", module.getModifiedItemAttr("capacity") or 0)
