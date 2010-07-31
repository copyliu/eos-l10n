#Used by:
#Subsystem: Loki Propulsion - Fuel Catalyst
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Propulsion Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Afterburner",
                                    "speedFactor", module.getModifiedItemAttr("subsystemBonusMinmatarPropulsion") * level)
