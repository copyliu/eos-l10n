#Used by:
#Ship: Bantam
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("shipBonusCF") * level)