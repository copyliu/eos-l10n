#Used by:
#Ship: Malediction
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.ship.boostItemAttr("armorKineticDamageResonance", ship.getModifiedItemAttr("shipBonus2AF") * level)