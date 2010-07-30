#Item: Merlin [Ship]
#Item: Worm [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.ship.boostItemAttr("shieldEmDamageResonance", ship.getModifiedItemAttr("shipBonusCF") * level)