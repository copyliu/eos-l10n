#Item: 'Smokescreen' Covert Ops Cloaking Device II [Module]
#Item: Covert Ops Cloaking Device II [Module]
type = "active"
def handler(fit, ship, context):
    fit.ship.cloaked = True
    #TODO: Implement