#Item: Siege Warfare Mindlink [Implant]
def handler(fit, implant, context):
    fit.character.getSkill("Siege Warfare Specialist").suppress()
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Siege Warfare Specialist"),
                                  "commandBonus", implant.getModifiedItemAttr("mindlinkBonus"))