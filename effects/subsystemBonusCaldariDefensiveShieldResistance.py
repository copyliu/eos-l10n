#Item: Tengu Defensive - Adaptive Shielding [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Defensive Systems").level
    for type in ("Em", "Kinetic", "Thermal", "Explosive"):
        fit.ship.boostItemAttr("shield%sDamageResonance" % type, module.getModifiedItemAttr("subsystemBonusCaldariDefensive") * level)