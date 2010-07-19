#Variations of item: Griffin (2 of 2) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "ECM",
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusCF2") * level)