#Item: Legion Defensive - Adaptive Augmenter [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Projector",
                                  "armorDamageAmount", module.getModifiedItemAttr("subsystemBonusAmarrDefensive2") * level)