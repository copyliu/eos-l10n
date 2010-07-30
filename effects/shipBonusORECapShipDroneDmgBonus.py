#Item: Rorqual [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Capital Industrial Ships").level
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Combat Drone",
                                 "damageMultiplier", ship.getModifiedItemAttr("shipBonusORECapital4") * level)