#Items from group: Ballistic Control system (21 of 21) [Module]
type = "passive"
def handler(fit, container, context):
    for dmgType in ("em", "kinetic", "explosive", "thermal"):
        fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "%sDamage" % dmgType, container.getModifiedItemAttr("missileDamageMultiplierBonus"),
                                    stackingPenalties = True)