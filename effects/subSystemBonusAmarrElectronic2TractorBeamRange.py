#Item: Legion Electronics - Emergent Locus Analyzer [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tractor Beam",
                                  "maxRange", module.getModifiedItemAttr("subsystemBonusAmarrElectronic2") * level)
