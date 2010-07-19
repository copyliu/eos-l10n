#Items from market group: Ships > Carriers > Gallente (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Carrier").level
    fit.ship.maxActiveDrones += ship.getModifiedItemAttr("carrierGallenteBonus1") * level