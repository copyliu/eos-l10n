#Item: Tormentor [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Mining Laser",
                                  "miningAmount", ship.getModifiedItemAttr("shipBonus2AF") * level)