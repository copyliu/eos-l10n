#Item: Leviathan [Ship]
type = "gang", "passive"
def handler(fit, ship, context):
    if "ship" in context:
        level = fit.character.getSkill("Caldari Titan").level
        fit.ship.multiplyItemAttr("shipBonusCT2", level)
    elif "gang" in context:
        fit.ship.boostItemAttr("shieldCapacity", ship.getModifiedItemAttr("shipBonusCT2"))
