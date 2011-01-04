#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMD (3 of 3)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Defender Missiles"),
                                       "maxVelocity", container.getModifiedItemAttr("missileVelocityBonus"))