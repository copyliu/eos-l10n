#Used by:
#Subsystems from group: Propulsion Systems (16 of 16)
runTime = "early"
type = "passive"
def handler(fit, module, context):
    fit.ship.itemModifiedAttributes["agility"] = module.getModifiedItemAttr("agility")