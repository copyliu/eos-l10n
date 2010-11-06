#Used by:
#Ship: Tormentor
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Mining Laser",
                                  "miningAmount", ship.getModifiedItemAttr("shipBonus2AF") * level)
