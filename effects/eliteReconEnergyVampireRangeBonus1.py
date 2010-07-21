#Item: Curse [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Recon Ships").level
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name == "Energy Vampire",
                                    "powerTransferRange", ship.getModifiedItemAttr("eliteBonusReconShip1") * level)