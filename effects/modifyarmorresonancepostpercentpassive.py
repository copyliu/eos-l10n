# Used by:
# Modules named like: Anti Pump (24 of 24)
type = "passive"
def handler(fit, module, context):
    for type in ("kinetic", "thermal", "explosive", "em"):
        fit.ship.boostItemAttr("armor" + type.capitalize() + "DamageResonance",
                               module.getModifiedItemAttr(type + "DamageResistanceBonus") or 0,
                               stackingPenalties = True)
