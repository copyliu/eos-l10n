#Variations of item: Bellicose (3 of 3) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Target Painter",
                                  "signatureRadiusBonus", ship.getModifiedItemAttr("shipBonusMC2") * level)