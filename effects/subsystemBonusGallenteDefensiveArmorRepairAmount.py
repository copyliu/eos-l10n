# Used by:
# Subsystem: Proteus Defensive - Nanobot Injector
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", module.getModifiedItemAttr("subsystemBonusGallenteDefensive") * level)
