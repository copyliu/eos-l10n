#Used by:
#Modules from group: Armor Coating (201 of 201)
#Modules from group: Armor Plating Energized (187 of 187)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("armorHP", module.getModifiedItemAttr("armorHPMultiplier"))