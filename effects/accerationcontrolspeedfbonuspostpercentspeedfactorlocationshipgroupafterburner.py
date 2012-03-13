# Used by:
# Implants named like: Hardwiring Eifyr and Co. 'Rogue' MY (6 of 6)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Propulsion Module",
                                  "speedFactor", implant.getModifiedItemAttr("speedFBonus"))
