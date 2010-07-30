#Used by:
#Subsystem: Proteus Defensive - Adaptive Augmenter
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Defensive Systems").level
    for type in ("Em", "Kinetic", "Thermal", "Explosive"):
        fit.ship.boostItemAttr("armor%sDamageResonance" % type,
                               module.getModifiedItemAttr("subsystemBonusGallenteDefensive") * level)
