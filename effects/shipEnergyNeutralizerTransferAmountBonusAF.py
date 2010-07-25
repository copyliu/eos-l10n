#Item: Cruor [Ship]
#Item: Sentinel [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Destabilizer",
                                  "energyDestabilizationAmount", ship.getModifiedItemAttr("shipBonusAF") * level)