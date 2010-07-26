#Item: Loki Defensive - Amplification Node [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Defensive Systems").level
    fit.ship.boostItemAttr("signatureRadius", module.getModifiedItemAttr("subsystemBonusMinmatarDefensive") * level)