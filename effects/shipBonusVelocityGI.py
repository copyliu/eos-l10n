#Items from market group: Ships > Industrial Ships > Gallente (5 of 7)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Industrial").level
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("shipBonusGI") * level)