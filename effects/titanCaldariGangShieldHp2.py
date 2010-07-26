#Item: Leviathan [Ship]
type = "gang", "passive"
def handler(fit, ship, context):
    if context == "ship":
        level = fit.character.getSkill("Caldari Titan").level
        fit.ship.multiplyItemAttr("shipBonusCT2", level)
    elif context == "gang":
        fit.ship.boostItemAttr("shieldCapacity", ship.getModifiedItemAttr("shipBonusCT2"))