#Item: Loki Defensive - Warfare Processor [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Skirmish Warfare Specialist"),
                                  "commandBonus", module.getModifiedItemAttr("subsystemBonusMinmatarDefensive") * level)
