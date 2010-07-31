#Used by:
#Ship: Exequror
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Frigate").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("shipBonusGC2") * level)