#Item: Tengu Engineering - Capacitor Regeneration Matrix [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Engineering Systems").level
    fit.ship.boostItemAttr("rechargeRate", module.getModifiedItemAttr("subsystemBonusCaldariEngineering") * level)
