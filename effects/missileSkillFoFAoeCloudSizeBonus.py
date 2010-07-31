#Used by:
#Implants named like: Hardwiring Zainou 'Snapshot' ZMF (3 of 3)
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("FoF Missiles"),
                                    "aoeCloudSize", container.getModifiedItemAttr("aoeCloudSizeBonus") * level)
