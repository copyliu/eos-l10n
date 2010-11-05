#Used by:
#Ships named like: Augoror (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.ship.boostItemAttr("armorHP", ship.getModifiedItemAttr("shipBonusAC2") * level)
