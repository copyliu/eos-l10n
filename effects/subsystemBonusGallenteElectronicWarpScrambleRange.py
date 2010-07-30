#Item: Proteus Electronics - Friction Extension Processor [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Warp Scrambler",
                                  "maxRange", module.getModifiedItemAttr("subsystemBonusGallenteElectronic") * level)
