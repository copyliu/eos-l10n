type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.requiresSkill("Armored Warfare Specialist"),
                                  "commandBonus", implant.getModifiedItemAttr("mindlinkBonus"))