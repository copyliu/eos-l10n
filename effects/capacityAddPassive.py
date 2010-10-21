#Used by:
#Subsystems from group: Defensive Systems (16 of 16)
type = "passive"
def handler(fit, subsystem, context):
    fit.extraAttributes.increase("capacity", subsystem.item.capacity or 0)
