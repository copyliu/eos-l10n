#Used by:
#Ship: Imicus
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Frigate").level
    fit.extraAttributes.boost("droneControlRange", ship.getModifiedItemAttr("shipBonusGF") * level)
