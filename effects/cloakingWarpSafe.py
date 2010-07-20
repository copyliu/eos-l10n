#Item: 'Smokescreen' Covert Ops Cloaking Device II [Module]
#Item: Covert Ops Cloaking Device II [Module]
type = "active"
runTime = "early"
def handler(fit, ship, context):
    fit.cloaked = True
    #TODO: Implement