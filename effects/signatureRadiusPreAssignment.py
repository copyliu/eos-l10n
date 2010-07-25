#Items from group: Defensive Systems (16 of 16) [Subsystem]
runTime = "early"
def handler(fit, module, context):
    fit.ship.itemModifiedAttributes["signatureRadius"] = module.getModifiedItemAttr("signatureRadius")