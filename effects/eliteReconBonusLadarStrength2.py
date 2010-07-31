#Used by:
#Ship: Falcon
#Ship: Rook
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Recon Ships").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "ECM",
                                  "scanLadarStrengthBonus", ship.getModifiedItemAttr("eliteBonusReconShip2") * level)