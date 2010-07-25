#Item: Ashimmu [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Destabilizer",
                                  "energyDestabilizationAmount", ship.getModifiedItemAttr("shipBonusAC") * level)