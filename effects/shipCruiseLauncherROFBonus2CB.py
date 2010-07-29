#Items with name like: Raven (3 of 3)
#Item: Scorpion Navy Issue [Ship]
#Item: Widow [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Missile Launcher Cruise",
                                    "speed", ship.getModifiedItemAttr("shipBonus2CB") * level)