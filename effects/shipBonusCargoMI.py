#Variations of item: Mammoth (2 of 2) [Ship]
#Variations of item: Wreathe (2 of 2) [Ship]
#Item: Hoarder [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Industrial").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("shipBonusMI") * level)