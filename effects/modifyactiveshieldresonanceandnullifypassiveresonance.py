# Used by:
# Modules from group: Shield Hardener (97 of 97)
type = "active"
def handler(fit, module, context):
    for damageType in ("kinetic", "thermal", "explosive", "em"):
        fit.ship.boostItemAttr("shield" + damageType.capitalize() + "DamageResonance",
                               module.getModifiedItemAttr(damageType + "DamageResistanceBonus"),
                               stackingPenalties = True)
        module.multiplyItemAttr("passive" + damageType.capitalize() + "DamageResistanceBonus", 0)
