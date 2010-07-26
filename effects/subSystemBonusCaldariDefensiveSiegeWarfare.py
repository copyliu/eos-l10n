#Item: Tengu Defensive - Warfare Processor [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Siege Warfare Specialist"),
                                  "commandBonus", module.getModifiedItemAttr("subsystemBonusCaldariDefensive") * level)