#Variations of item: Raven (4 of 4) [Ship]
#Item: Widow [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.charge.requiresSkill("Torpedoes"),
                                  "maxVelocity", ship.getModifiedItemAttr("shipBonusCB3") * level)