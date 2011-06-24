# Used by:
# Subsystem: Legion Defensive - Nanobot Injector
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", module.getModifiedItemAttr("subsystemBonusAmarrDefensive") * level)
