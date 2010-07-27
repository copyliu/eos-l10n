#Item: Hulk [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Exhumers").level
    groups = "Strip Miner", "Frequency Mining Laser"
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "miningAmount", ship.getModifiedItemAttr("eliteBonusBarge1") * level)