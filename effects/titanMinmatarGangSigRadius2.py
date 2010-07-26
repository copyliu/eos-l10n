#Item: Ragnarok [Ship]
type = "gang", "passive"
def handler(fit, ship, context):
    if context == "ship":
        level = fit.character.getSkill("Minmatar Titan").level
        fit.ship.multiplyItemAttr("titanMinmatarBonus2", level)
    elif context == "gang":
        fit.ship.boostItemAttr("signatureRadius", ship.getModifiedItemAttr("titanMinmatarBonus2"))