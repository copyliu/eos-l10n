#Used by:
#Modules named like: Anti Screen Reinforcer (24 of 24)
type = "passive"
def handler(fit, module, context):
    for type in ("kinetic", "thermal", "explosive", "em"):
        targetAttrName = "shield" + type.capitalize() + "DamageResonance"
        if targetAttrName in module.item.attributes:
            fit.ship.boostItemAttr(targetAttrName, module.getModifiedItemAttr(type + "DamageResistanceBonus"),
                                   stackingPenalties = True)
