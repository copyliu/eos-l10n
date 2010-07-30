#Item: Ragnarok [Ship]
type = "gang", "passive"
def handler(fit, ship, context):
    if "ship" in context:
        level = fit.character.getSkill("Minmatar Titan").level
        fit.ship.multiplyItemAttr("titanMinmatarBonus2", level)
    elif "gang" in context:
        fit.ship.boostItemAttr("signatureRadius", ship.getModifiedItemAttr("titanMinmatarBonus2"))
