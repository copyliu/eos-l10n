#Used by:
#Ship: Widow
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Black Ops").level
    sensorTypes = ("Gravimetric", "Ladar", "Magnetometric", "Radar")
    groups = ("ECM", "ECM Burst")
    for type in sensorTypes:
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups, "scan{0}StrengthBonus".format(type),
                                      ship.getModifiedItemAttr("eliteBonusBlackOps1") * level)
