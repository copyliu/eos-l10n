#Used by:
#Ship: Reaper
#Ship: Vigil
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Frigate").level
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("shipBonusMF") * level)
