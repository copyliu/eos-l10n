#Item: Loki Defensive - Adaptive Shielding [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Defensive Systems").level
    for type in ("Em", "Kinetic", "Thermal", "Explosive"):
        fit.ship.boostItemAttr("shield%sDamageResonance" % type, module.getModifiedItemAttr("subsystemBonusMinmatarDefensive") * level)
