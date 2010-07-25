#Item: Ashimmu [Ship]
#Item: Vigilant [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Stasis Web",
                                  "speedFactor", ship.getModifiedItemAttr("shipBonusMC2") * level)