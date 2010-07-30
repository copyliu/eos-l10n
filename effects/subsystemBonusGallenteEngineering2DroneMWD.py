#Item: Proteus Engineering - Augmented Capacitor Reservoir [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Engineering Systems").level
    fit.drones.filteredItemBoost(lambda drone: True, "maxVelocity",
                                 module.getModifiedItemAttr("subsystemBonusGallenteEngineering2") * level)
