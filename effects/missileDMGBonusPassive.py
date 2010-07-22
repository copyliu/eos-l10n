#Variations of item: Large Warhead Calefaction Catalyst I (2 of 2) [Module]
#Variations of item: Medium Warhead Calefaction Catalyst I (2 of 2) [Module]
#Variations of item: Small Warhead Calefaction Catalyst I (2 of 2) [Module]
type = "passive"
def handler(fit, container, context):
    for dmgType in ("em", "kinetic", "explosive", "thermal"):
        fit.modules.filteredChargeMultiply(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                           "%sDamage" % dmgType, container.getModifiedItemAttr("missileDamageMultiplierBonus"),
                                           stackingPenalties = True)