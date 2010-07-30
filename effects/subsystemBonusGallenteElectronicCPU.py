#Item: Proteus Electronics - CPU Efficiency Gate [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Electronic Systems").level
    fit.ship.boostItemAttr("cpuOutput", module.getModifiedItemAttr("subsystemBonusGallenteElectronic") * level)
