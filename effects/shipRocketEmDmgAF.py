#Item: Anathema [Ship]
#Item: Malediction [Ship]
#Item: Vengeance [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Rockets"),
                                  "emDamage", ship.getModifiedItemAttr("shipBonusAF") * level)