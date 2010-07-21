#Item: Guardian [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Logistics").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Projector",
                                  "capacitorNeed", ship.getModifiedItemAttr("eliteBonusLogistics2") * level)