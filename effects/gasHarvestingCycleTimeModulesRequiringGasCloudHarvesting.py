#Item: Hardwiring - Eifyr and Co. 'Alchemist' ZA-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' ZA-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' ZA-2 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gas Cloud Harvesting"),
                                  "duration", implant.getModifiedItemAttr("durationBonus"))