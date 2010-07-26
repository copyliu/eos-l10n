#Item: Legion Defensive - Augmented Plating [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Defensive Systems").level
    fit.ship.boostItemAttr("armorHP", module.getModifiedItemAttr("subsystemBonusAmarrDefensive") * level)