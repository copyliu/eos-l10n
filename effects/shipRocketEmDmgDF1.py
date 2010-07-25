#Item: Heretic [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Destroyers").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Rockets"),
                                  "emDamage", ship.getModifiedItemAttr("shipBonusDF1") * level)