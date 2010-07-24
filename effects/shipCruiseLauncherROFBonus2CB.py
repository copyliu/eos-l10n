#Variations of item: Raven (3 of 4) [Ship]
#Item: Scorpion Navy Issue [Ship]
#Item: Widow [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Missile Launcher Cruise",
                                    "speed", ship.getModifiedItemAttr("shipBonus2CB") * level)