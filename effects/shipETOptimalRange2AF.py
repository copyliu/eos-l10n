#Item: Imperial Navy Slicer [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "maxRange", ship.getModifiedItemAttr("shipBonus2AF") * level)