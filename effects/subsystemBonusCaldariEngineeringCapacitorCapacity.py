#Item: Tengu Engineering - Augmented Capacitor Reservoir [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Engineering Systems").level
    fit.ship.boostItemAttr("capacitorCapacity", module.getModifiedItemAttr("subsystemBonusCaldariEngineering") * level)
