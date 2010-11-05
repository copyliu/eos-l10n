#Used by:
#Ships from group: Black Ops (4 of 4)
#Ships from group: Stealth Bomber (4 of 4)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemForce(lambda mod: mod.item.group.name == "Cloaking Device",
                                  "cloakingTargetingDelay", ship.getModifiedItemAttr("covertOpsStealthBomberTargettingDelay"))
