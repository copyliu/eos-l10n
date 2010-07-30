#Item: Absolution [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Command Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("eliteBonusCoverOps1") * level)