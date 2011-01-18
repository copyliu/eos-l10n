#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Gunslinger' CX (6 of 6)
#Implant: Cerebral Accelerator
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "damageMultiplier", implant.getModifiedItemAttr("damageMultiplierBonus"))
