#Items from group: Armor Coating (201 of 201) [Module]
#Items from group: Armor Plating Energized (187 of 187) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("armorHP", module.getModifiedItemAttr("armorHPMultiplier"))