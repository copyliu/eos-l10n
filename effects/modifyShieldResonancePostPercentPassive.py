#Used by:
#Modules named like: Anti Screen Reinforcer (24 of 24)
type = "passive"
def handler(fit, module, context):
    for type in ("kinetic", "thermal", "explosive", "em"):
        fit.ship.boostItemAttr("shield" + type.capitalize() + "DamageResonance",
                               module.getModifiedItemAttr(type + "DamageResistanceBonus") or 0,
                               stackingPenalties = True)
