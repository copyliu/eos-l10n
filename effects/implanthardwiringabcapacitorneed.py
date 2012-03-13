# Used by:
# Implants named like: Hardwiring Eifyr and Co. 'Rogue' DY (6 of 6)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Propulsion Module"),
                                  "capacitorNeed", implant.getModifiedItemAttr("capNeedBonus"))
