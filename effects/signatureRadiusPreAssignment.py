#Used by:
#Subsystems from group: Defensive Systems (16 of 16)
type = "passive"
runTime = "early"
def handler(fit, module, context):
    fit.ship.forceItemAttr("signatureRadius", module.getModifiedItemAttr("signatureRadius"))
