#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Alchemist' ZA (3 of 3)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gas Cloud Harvesting"),
                                  "duration", implant.getModifiedItemAttr("durationBonus"))