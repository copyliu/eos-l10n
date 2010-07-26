#Item: Thermodynamics [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: "heatDamage" in mod.itemModifiedAttributes,
                                  "heatDamage", skill.getModifiedItemAttr("thermodynamicsHeatDamage") * level)