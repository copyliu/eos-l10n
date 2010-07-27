#Items from market group: Ships > Recon Ships > Minmatar (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Recon Ships").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Stasis Web",
                                    "maxRange", ship.getModifiedItemAttr("eliteBonusReconShip2") * level)