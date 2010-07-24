#Item: Hound [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Torpedoes"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusMF2") * level)