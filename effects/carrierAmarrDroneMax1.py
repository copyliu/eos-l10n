#Used by:
#Ship: Aeon
#Ship: Archon
#Ship: Revenant
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Carrier").level
    amount = ship.getModifiedItemAttr("carrierAmarrBonus1")
    fit.extraAttributes.increase("maxActiveDrones", amount * level)
