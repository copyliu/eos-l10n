#Item: Legion Electronics - Energy Parasitic Complex [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Destabilizer",
                                  "energyDestabilizationAmount", module.getModifiedItemAttr("subsystemBonusAmarrElectronic") * level)