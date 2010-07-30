#Used by:
#Ships named like: Iteron (5 of 5)
#Items from market group: Ships > Transport Ships > Gallente (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Industrial").level
    bonus = "shipBonusGI" if "Iteron" in ship.name else "shipBonusGI2" 
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr(bonus) * level)