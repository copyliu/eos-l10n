#Item: Nemesis [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Covert Ops").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Bomb Deployment"),
                                    "thermalDamage", ship.getModifiedItemAttr("eliteBonusCoverOps1") * level)