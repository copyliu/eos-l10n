#Used by:
#Ship: Worm
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Frigate").level
    fit.ship.boostItemAttr("droneCapacity", ship.getModifiedItemAttr("shipBonusGF") * level)