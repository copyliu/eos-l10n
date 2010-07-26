#Item: Loki Engineering - Capacitor Regeneration Matrix [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Engineering Systems").level
    fit.ship.boostItemAttr("rechargeRate", module.getModifiedItemAttr("subsystemBonusMinmatarEngineering") * level)