#Item: Improved Exile Booster [Implant]
#Item: Standard Exile Booster [Implant]
#Item: Strong Exile Booster [Implant]
#Item: Synth Exile Booster [Implant]
type = "passive"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", booster.getModifiedItemAttr("armorDamageAmountBonus"))