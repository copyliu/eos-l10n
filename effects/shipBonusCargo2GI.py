#Items from market group: Ships > Industrial Ships > Gallente (5 of 7)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Industrial").level
    bonus = "shipBonusGI" if "Iteron" in ship.name else "shipBonusGI2" 
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr(bonus) * level)