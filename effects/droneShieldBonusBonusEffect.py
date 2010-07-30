#Item: Basilisk [Ship]
#Item: Scimitar [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("%s Cruiser" % ship.item.race.capitalize()).level
    fit.drones.filteredItemBoost(lambda drone: "Shield Maintenance Bot" in drone.item.name,
                                 "shieldBonus", ship.getModifiedItemAttr("droneShieldBonusBonus") * level)