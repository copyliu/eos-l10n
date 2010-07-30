#Item: Hound [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Covert Ops").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Bomb Deployment"),
                                    "explosiveDamage", ship.getModifiedItemAttr("eliteBonusCoverOps1") * level)