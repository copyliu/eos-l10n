#Item: Avatar [Ship]
type = "gang", "passive"
def handler(fit, ship, context):
    if context == "ship":
        level = fit.character.getSkill("Amarr Titan").level
        fit.ship.multiplyItemAttr("titanAmarrBonus2", level)
    elif context == "gang":
        fit.ship.boostItemAttr("rechargeRate", ship.getModifiedItemAttr("titanAmarrBonus2"))