#Item: Impel [Ship]
#Item: Occator [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Transport Ships").level
    fit.ship.boostItemAttr("armorHP", ship.getModifiedItemAttr("shipBonusHPExtender1") * level)