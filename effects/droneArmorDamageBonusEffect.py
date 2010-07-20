#Item: Guardian [Ship]
#Item: Oneiros [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("%s Cruiser" % ship.item.race.capitalize()).level
    fit.drones.filteredItemBoost(lambda drone: "Armor Maintenance Bot" in drone.item.name,
                                 "armorDamageAmount", ship.getModifiedItemAttr("droneArmorDamageAmountBonus") * level)