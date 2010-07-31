#Used by:
#Ship: Arazu
#Ship: Lachesis
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Recon Ships").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Warp Scrambler",
                                    "maxRange", ship.getModifiedItemAttr("eliteBonusReconShip2") * level)