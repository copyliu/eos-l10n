#Item: Loki Engineering - Power Core Multiplier [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Engineering Systems").level
    fit.ship.boostItemAttr("powerOutput", module.getModifiedItemAttr("subsystemBonusMinmatarEngineering") * level)