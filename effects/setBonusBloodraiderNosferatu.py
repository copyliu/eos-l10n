#Items from group: Cyberimplant (10 of 138) [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Energy Emission Systems"),
                                  "duration", implant.getModifiedItemAttr("durationBonus"))