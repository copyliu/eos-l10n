# Used by:
# Modules from group: Remote Hull Repairer (4 of 4)
type = "projected", "active"
runTime = "late"
def handler(fit, module, context):
    if "projected" not in context: return
    bonus = module.getModifiedItemAttr("structureDamageAmount")
    duration = module.getModifiedItemAttr("duration") / 1000.0
    fit.extraAttributes.increase("hullRepair", bonus / duration)
