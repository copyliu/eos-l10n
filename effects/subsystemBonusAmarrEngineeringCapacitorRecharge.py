#Item: Legion Engineering - Capacitor Regeneration Matrix [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Engineering Systems").level
    fit.ship.boostItemAttr("rechargeRate", module.getModifiedItemAttr("subsystemBonusAmarrEngineering") * level)