#Item: Rattlesnake [Ship]
#Item: Rokh [Ship]
#Item: Scorpion Navy Issue [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.ship.boostItemAttr("shieldKineticDamageResonance", ship.getModifiedItemAttr("shipBonus2CB") * level)