#Variations of item: Raven (3 of 4) [Ship]
#Item: Scorpion Navy Issue [Ship]
#Item: Widow [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Siege",
                                  "speed", ship.getModifiedItemAttr("shipBonus2CB") * level)