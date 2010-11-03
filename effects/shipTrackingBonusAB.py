#Used by:
#Ship: Nightmare
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                  "trackingSpeed", ship.getModifiedItemAttr("shipBonusAB2") * level)
