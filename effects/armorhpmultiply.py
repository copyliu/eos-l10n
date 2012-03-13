# Used by:
# Modules from group: Armor Coating (201 of 201)
# Modules from group: Armor Plating Energized (187 of 187)
# Modules named like: QA Multiship Module Players (4 of 4)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("armorHP", module.getModifiedItemAttr("armorHPMultiplier"))