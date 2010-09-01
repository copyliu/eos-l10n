#Used by:
#Modules named like: Anti Screen Reinforcer (24 of 24)
type = "passive"
def handler(fit, module, context):
    for type in ("kinetic", "thermal", "explosive", "em"):
        targetAttrName = "shield" + type.capitalize() + "DamageResonance"
        fit.ship.boostItemAttr(targetAttrName, module.getModifiedItemAttr(type + "DamageResistanceBonus") or 0,
                               stackingPenalties = True)
