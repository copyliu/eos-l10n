#Item: Tengu Propulsion - Fuel Catalyst [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Propulsion Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                    "speedFactor", module.getModifiedItemAttr("subsystemBonusCaldariPropulsion") * level)