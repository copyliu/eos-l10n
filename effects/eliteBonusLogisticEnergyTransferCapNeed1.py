#Item: Guardian [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Logistics").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Transfer Array",
                                  "capacitorNeed", ship.getModifiedItemAttr("eliteBonusLogistics1") * level)