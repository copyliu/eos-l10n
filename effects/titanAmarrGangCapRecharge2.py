#Item: Avatar [Ship]
type = "gang", "passive"
def handler(fit, ship, context):
    if "ship" in context:
        level = fit.character.getSkill("Amarr Titan").level
        fit.ship.multiplyItemAttr("titanAmarrBonus2", level)
    elif "gang" in context:
        fit.ship.boostItemAttr("rechargeRate", ship.getModifiedItemAttr("titanAmarrBonus2"))
