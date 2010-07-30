#Item: Doomsday Operation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Super Weapon" and "emDamage" in mod.itemModifiedAttributes,
                                  "emDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Super Weapon" and "thermalDamage" in mod.itemModifiedAttributes,
                                  "thermalDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Super Weapon" and "kineticDamage" in mod.itemModifiedAttributes,
                                  "kineticDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Super Weapon" and "explosiveDamage" in mod.itemModifiedAttributes,
                                  "explosiveDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
