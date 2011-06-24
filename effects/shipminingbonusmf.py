# Used by:
# Ship: Burst
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Mining Laser",
                                  "miningAmount", ship.getModifiedItemAttr("shipBonusMF") * level)
