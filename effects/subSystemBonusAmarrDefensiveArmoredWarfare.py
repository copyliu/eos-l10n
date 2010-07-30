#Item: Legion Defensive - Warfare Processor [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Armored Warfare Specialist"),
                                  "commandBonus", module.getModifiedItemAttr("subsystemBonusAmarrDefensive") * level)
