#Item: Tengu Electronics - Obfuscation Manifold [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Electronic Systems").level
    fit.modules.filteredItemBoost(mod.group.name == "ECM",
                                  "maxRange", module.getModifiedItemAttr("subsystemBonusCaldariElectronic") * level)