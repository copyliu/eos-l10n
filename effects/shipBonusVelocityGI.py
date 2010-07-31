#Used by:
#Ships named like: Iteron (5 of 5)
#Ship: Occator
#Ship: Viator
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Industrial").level
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("shipBonusGI") * level)