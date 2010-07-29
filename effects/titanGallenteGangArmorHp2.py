#Item: Erebus [Ship]
type = "gang", "passive"
def handler(fit, ship, context):
    if "ship" in context:
        level = fit.character.getSkill("Gallente Titan").level
        fit.ship.multiplyItemAttr("titanGallenteBonus2", level)
    elif "gang" in context:
        fit.ship.boostItemAttr("armorHP", ship.getModifiedItemAttr("titanGallenteBonus2"))
