#Item: Explosive Armor Compensation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Armor Hardener",
                                  "passiveExplosiveDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningbonus2"))