#Item: Purifier [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Torpedoes"),
                                    "aoeVelocity", ship.getModifiedItemAttr("shipBonusAF") * level)