#Items from group: Cloaking Device (12 of 14) [Module]
type = "active"
runTime = "early"
def handler(fit, module, context):
    fit.extraAttributes["cloaked"] = True
    #TODO: Rewrite this effect