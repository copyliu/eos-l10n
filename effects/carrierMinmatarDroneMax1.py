#Used by:
#Items from market group: Ships > Carriers > Minmatar (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Carrier").level
    amount = ship.getModifiedItemAttr("carrierMinmatarBonus1")
    fit.extraAttributes["maxActiveDrones"].increase(amount * level)