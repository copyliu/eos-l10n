# Used by:
# Ship: Burst
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Frigate").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("shipBonusMF2") * level)
