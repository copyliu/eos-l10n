#Item: Scimitar [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Logistics").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Tracking Link",
                                  "falloffBonus", ship.getModifiedItemAttr("eliteBonusLogistics1") * level)