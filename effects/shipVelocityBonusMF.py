#Used by:
#Ship: Vigil
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Frigate")
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("shipBonusMF") * level)