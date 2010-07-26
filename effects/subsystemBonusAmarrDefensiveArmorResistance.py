#Item: Legion Defensive - Adaptive Augmenter [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Defensive Systems").level
    for type in ("Em", "Kinetic", "Thermal", "Explosive"):
        fit.ship.boostItemAttr("armor%sDamageResonance" % type, module.getModifiedItemAttr("subsystemBonusAmarrDefensive") * level)