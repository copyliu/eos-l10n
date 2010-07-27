#Item: Warfare Link Specialist [Skill]
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Gang Coordinator" and \
                                  "commandBonus" in mod.itemModifiedAttributes,
                                  "commandBonus", skill.getModifiedItemAttr("squadronCommandBonus") * skill.level)