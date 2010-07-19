#Items from market group: Ships > Carriers > Amarr (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Carrier").level
    fit.ship.maxActiveDrones += ship.getModifiedItemAttr("carrierAmarrBonus1") * level