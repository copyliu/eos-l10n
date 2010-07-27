#Item: Tengu Defensive - Adaptive Shielding [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Transporter",
                                  "shieldBonus", module.getModifiedItemAttr("subsystemBonusCaldariDefensive2") * level)