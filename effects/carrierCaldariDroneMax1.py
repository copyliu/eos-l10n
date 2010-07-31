#Used by:
#Ship: Chimera
#Ship: Wyvern
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Carrier").level
    amount = ship.getModifiedItemAttr("carrierCaldariBonus1")
    fit.extraAttributes["maxActiveDrones"].increase(amount * level)