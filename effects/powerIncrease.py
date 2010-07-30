#Used by:
#Modules from group: Auxiliary Power Core (7 of 7)
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("powerOutput", module.getModifiedItemAttr("powerIncrease"))