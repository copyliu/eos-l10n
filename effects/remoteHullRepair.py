#Items from group: Remote Hull Repairer (4 of 4) [Module]
type = "projected", "active"
runTime = "late"
def handler(fit, module, context):
    if context != "projected": return
    amount = module.getModifiedItemAttr("structureDamageAmount")
    duration = module.getModifiedItemAttr("duration") / 1000.0
    fit.hullRepair += amount / duration