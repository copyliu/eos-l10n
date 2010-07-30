#Item: Proteus Defensive - Augmented Plating [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Defensive Systems").level
    fit.ship.boostItemAttr("armorHP", module.getModifiedItemAttr("subsystemBonusGallenteDefensive") * level)
