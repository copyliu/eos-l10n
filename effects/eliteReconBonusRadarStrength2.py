#Items from market group: Ships > Recon Ships > Caldari (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Recon Ships").level
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name == "ECM",
                                  "scanRadarStrengthBonus", ship.getModifiedItemAttr("eliteBonusReconShip2") * level)