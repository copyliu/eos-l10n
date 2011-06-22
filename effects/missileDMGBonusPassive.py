# Used by:
# Modules named like: Warhead Calefaction Catalyst (6 of 6)
type = "passive"
def handler(fit, container, context):
    for dmgType in ("em", "kinetic", "explosive", "thermal"):
        fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                           "%sDamage" % dmgType, container.getModifiedItemAttr("missileDamageMultiplierBonus"),
                                           stackingPenalties = True)