# Used by:
# Ship: Impel
# Ship: Occator
# Ship: Prorator
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Transport Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", ship.getModifiedItemAttr("eliteBonusIndustrial1") * level)
