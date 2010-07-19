#Items from market group: Ships > Carriers > Caldari (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Carrier").level
    fit.ship.maxActiveDrones += ship.getModifiedItemAttr("carrierCaldariBonus1") * level