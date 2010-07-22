#Item: Information Warfare Mindlink [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Information Warfare Specialist"),
                                  "commandBonus", implant.getModifiedItemAttr("mindlinkBonus"))