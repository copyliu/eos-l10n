#Item: Legion Engineering - Augmented Capacitor Reservoir [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Engineering Systems").level
    fit.ship.boostItemAttr("capacitorCapacity", module.getModifiedItemAttr("subsystemBonusAmarrEngineering") * level)