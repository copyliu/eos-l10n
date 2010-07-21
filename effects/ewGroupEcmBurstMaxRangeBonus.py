#Item: Low-grade Centurion Alpha [Implant]
#Item: Low-grade Centurion Beta [Implant]
#Item: Low-grade Centurion Delta [Implant]
#Item: Low-grade Centurion Epsilon [Implant]
#Item: Low-grade Centurion Gamma [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Remote ECM Burst",
                                  "maxRange", implant.getModifiedItemAttr("rangeSkillBonus"))