# Used by:
# Ships named like: Iteron (5 of 5)
# Ship: Occator
# Ship: Viator
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Industrial").level
    # TODO: investigate if we can live without such ifs or hardcoding
    # Viator doesn't have GI bonus
    if "shipBonusGI" in fit.ship.item.attributes:
        bonusAttr = "shipBonusGI"
    else:
        bonusAttr = "shipBonusGI2"
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr(bonusAttr) * level)
