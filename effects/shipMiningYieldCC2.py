#Used by:
#Ship: Osprey
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Mining Laser",
                                  "miningAmount", ship.getModifiedItemAttr("shipBonusCC2") * level)