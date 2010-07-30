#Item: Malediction [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.ship.boostItemAttr("armorExplosiveDamageResonance", ship.getModifiedItemAttr("shipBonus2AF") * level)