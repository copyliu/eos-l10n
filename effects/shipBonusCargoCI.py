#Variations of item: Badger (2 of 2) [Ship]
#Variations of item: Badger Mark II (2 of 2) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Industrial").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("shipBonusCI") * level)