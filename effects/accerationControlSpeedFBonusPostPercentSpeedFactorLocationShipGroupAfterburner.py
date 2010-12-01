#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Rogue' MY (3 of 3)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "speedFactor", implant.getItemAttr("speedFBonus"))