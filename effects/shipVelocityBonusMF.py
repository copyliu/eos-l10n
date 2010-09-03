#Used by:
#Ship: Vigil
type = "passive"
def handler(fit, ship, context):
    skill = fit.character.getSkill("Minmatar Frigate").level
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("shipBonusMF") * skill.level)
