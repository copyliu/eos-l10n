#Item: Tengu Engineering - Power Core Multiplier [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Engineering Systems").level
    fit.ship.boostItemAttr("powerOutput", module.getModifiedItemAttr("subsystemBonusCaldariEngineering") * level)