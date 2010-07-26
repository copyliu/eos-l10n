#Item: Loki Defensive - Adaptive Shielding [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Transporter",
                                  "shieldBonus", module.getModifiedItemAttr("subsystemBonusMinmatarDefensive2") * level)