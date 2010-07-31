#Used by:
#Ship: Basilisk
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Transfer Array",
                                  "powerTransferRange", ship.getModifiedItemAttr("shipBonusCC2") * level)