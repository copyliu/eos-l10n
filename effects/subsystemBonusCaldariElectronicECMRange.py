#Item: Tengu Electronics - Obfuscation Manifold [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Electronic Systems").level
    fit.modules.filteredItemBoost(mod.item.group.name == "ECM",
                                  "maxRange", module.getModifiedItemAttr("subsystemBonusCaldariElectronic") * level)
