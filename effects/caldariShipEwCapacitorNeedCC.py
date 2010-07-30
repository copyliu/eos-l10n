#Used by:
#Items from market group: Ships > Recon Ships > Caldari (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusCC") * level)