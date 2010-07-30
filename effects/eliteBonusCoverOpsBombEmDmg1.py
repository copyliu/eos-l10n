#Used by:
#Ship: Purifier
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Covert Ops").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Bomb Deployment"),
                                    "emDamage", ship.getModifiedItemAttr("eliteBonusCoverOps1") * level)