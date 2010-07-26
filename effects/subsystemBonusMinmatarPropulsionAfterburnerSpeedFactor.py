#Item: Loki Propulsion - Fuel Catalyst [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Propulsion Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name == "Afterburner"),
                                    "speedFactor", module.getModifiedItemAttr("subsystemBonusMinmatarPropulsion") * level)