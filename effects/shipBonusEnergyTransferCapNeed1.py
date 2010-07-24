#Item: Augoror [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Transfer Array",
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusAC") * level)