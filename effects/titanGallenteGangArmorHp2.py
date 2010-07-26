#Item: Erebus [Ship]
type = "gang", "passive"
def handler(fit, ship, context):
    if context == "ship":
        level = fit.character.getSkill("Gallente Titan").level
        fit.ship.multiplyItemAttr("titanGallenteBonus2", level)
    elif context == "gang":
        fit.ship.boostItemAttr("armorHP", ship.getModifiedItemAttr("titanGallenteBonus2"))