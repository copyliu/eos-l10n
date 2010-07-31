#Used by:
#Ship: Navitas
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Frigate").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("shipBonusGF2") * level)