#Used by:
#Subsystem: Loki Propulsion - Fuel Catalyst
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Propulsion Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "speedFactor", module.getModifiedItemAttr("subsystemBonusMinmatarPropulsion") * level)
