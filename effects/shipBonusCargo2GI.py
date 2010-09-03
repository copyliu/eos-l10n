#Used by:
#Ships named like: Iteron (5 of 5)
#Ship: Occator
#Ship: Viator
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Industrial").level
    bonus = "shipBonusGI" if "Iteron" in ship.item.name else "shipBonusGI2"
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr(bonus) * level)
