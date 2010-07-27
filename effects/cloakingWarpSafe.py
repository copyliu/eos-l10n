#Item: 'Smokescreen' Covert Ops Cloaking Device II [Module]
#Item: Covert Ops Cloaking Device II [Module]
type = "active"
runTime = "early"
def handler(fit, ship, context):
    fit.extraAttributes["cloaked"] = True
    #TODO: Implement