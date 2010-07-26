#Item: Proteus Electronics - CPU Efficiency Gate [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Electronic Systems").level
    fit.ship.boostItemAttr("cpuOutput", module.getModifiedItemAttr("subsystemBonusGallenteElectronic") * level)