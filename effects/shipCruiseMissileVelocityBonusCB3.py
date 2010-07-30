#Variations of item: Raven (4 of 4) [Ship]
#Item: Widow [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Cruise Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusCB3") * level)