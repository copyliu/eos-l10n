#Item: Damnation [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Command Ships").level
    fit.ship.boostItemAttr("armorHP", ship.getModifiedItemAttr("eliteBonusCommandShips1") * level)