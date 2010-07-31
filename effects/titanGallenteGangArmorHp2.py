#Item: Erebus [Ship]
type = "gang", "passive"
def handler(fit, ship, context):
    if "gang" in context:
        fit.ship.boostItemAttr("armorHP", ship.commandBonus)
    else:
        level = fit.character.getSkill("Gallente Titan").level
        ship.commandBonus = fit.ship.getModifiedItemAttr("titanGallenteBonus2") * level
