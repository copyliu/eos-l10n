#Item: Scimitar [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Logistics").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Tracking Link",
                                  "maxRangeBonus", ship.getModifiedItemAttr("eliteBonusLogistics1") * level)