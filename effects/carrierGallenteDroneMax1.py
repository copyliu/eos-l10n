#Used by:
#Ship: Nyx
#Ship: Thanatos
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Carrier").level
    amount = ship.getModifiedItemAttr("carrierGallenteBonus1")
    fit.extraAttributes["maxActiveDrones"].increase(amount * level)