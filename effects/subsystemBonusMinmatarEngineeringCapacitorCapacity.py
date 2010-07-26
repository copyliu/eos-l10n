#Item: Loki Engineering - Augmented Capacitor Reservoir [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Engineering Systems").level
    fit.ship.boostItemAttr("capacitorCapacity", module.getModifiedItemAttr("subsystemBonusMinmatarEngineering") * level)