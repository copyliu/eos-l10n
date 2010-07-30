#Item: Cerebral Accelerator [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' CX-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' CX-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' CX-2 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "damageMultiplier", implant.getModifiedItemAttr("damageMultiplierBonus"))
