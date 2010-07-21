#Item: Huginn [Ship]
#Item: Lachesis [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Recon Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Missile Launcher Assault",
                                  "speed", ship.getModifiedItemAttr("eliteBonusReconShip1") * level)