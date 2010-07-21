#Items from market group: Ships > Recon Ships > Amarr (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Recon Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Destabilizer",
                                  "energyDestabilizationRange", ship.getModifiedItemAttr("eliteBonusReconShip1") * level)