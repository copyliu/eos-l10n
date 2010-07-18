#Item: Armored Warfare Mindlink [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Armored Warfare Specialist"),
                                  "commandBonus", implant.getModifiedItemAttr("mindlinkBonus"))