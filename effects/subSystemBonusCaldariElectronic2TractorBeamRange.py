#Item: Tengu Electronics - Emergent Locus Analyzer [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tractor Beam",
                                  "maxRange", module.getModifiedItemAttr("subsystemBonusCaldariElectronic2") * level)
