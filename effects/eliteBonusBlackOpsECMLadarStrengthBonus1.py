#Used by:
#Ship: Widow
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Black Ops").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "scanLadarStrengthBonus", ship.getModifiedItemAttr("eliteBonusBlackOps1") * level)
