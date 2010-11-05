#Used by:
#Charge: Focused Warp Disruption
type = "passive"
def handler(fit, module, context):
    module.forceItemAttr("disallowInEmpireSpace", module.getModifiedChargeAttr("disallowInEmpireSpace"))
