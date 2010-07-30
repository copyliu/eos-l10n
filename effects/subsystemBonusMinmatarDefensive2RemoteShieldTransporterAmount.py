#Item: Loki Defensive - Adaptive Shielding [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Transporter",
                                  "shieldBonus", module.getModifiedItemAttr("subsystemBonusMinmatarDefensive2") * level)
