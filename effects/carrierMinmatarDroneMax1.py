#Items from market group: Ships > Carriers > Minmatar (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Carrier").level
    fit.ship.maxActiveDrones += ship.getModifiedItemAttr("carrierMinmatarBonus1") * level