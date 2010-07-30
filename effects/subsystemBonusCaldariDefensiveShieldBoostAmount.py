#Item: Tengu Defensive - Amplification Node [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "shieldBonus", module.getModifiedItemAttr("subsystemBonusCaldariDefensive") * level)
