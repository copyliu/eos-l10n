#Item: Proteus Engineering - Power Core Multiplier [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Engineering Systems").level
    fit.ship.boostItemAttr("powerOutput", module.getModifiedItemAttr("subsystemBonusGallenteEngineering") * level)
