#Item: Sentinel [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Tracking Disruptor",
                                  "trackingSpeedBonus", ship.getModifiedItemAttr("shipBonus2AF") * level)