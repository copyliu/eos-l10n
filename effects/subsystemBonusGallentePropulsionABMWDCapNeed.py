#Item: Proteus Propulsion - Localized Injectors [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Propulsion Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Afterburner"),
                                    "capacitorNeed", module.getModifiedItemAttr("subsystemBonusCaldariPropulsion") * level)