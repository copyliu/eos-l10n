#Item: Proteus Engineering - Capacitor Regeneration Matrix [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Engineering Systems").level
    fit.ship.boostItemAttr("rechargeRate", module.getModifiedItemAttr("subsystemBonusGallenteEngineering") * level)