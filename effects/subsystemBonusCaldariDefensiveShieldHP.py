#Item: Tengu Defensive - Supplemental Screening [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Defensive Systems").level
    fit.ship.boostItemAttr("shieldCapacity", module.getModifiedItemAttr("subsystemBonusCaldariDefensive") * level)