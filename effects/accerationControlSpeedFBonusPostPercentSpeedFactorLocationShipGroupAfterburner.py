#Item: Hardwiring - Eifyr and Co. 'Rogue' MY-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' MY-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' MY-2 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "speedFactor", implant.getItemAttr("speedFBonus"))