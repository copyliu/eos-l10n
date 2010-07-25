#Item: Skirmish Warfare Mindlink [Implant]
from customEffects import boostModListBySkillReq
def handler(fit, implant, context):
    fit.character.getSkill("Skirmish Warfare Specialist").suppress()
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Skirmish Warfare Specialist"),
                                  "commandBonus", implant.getModifiedItemAttr("mindlinkBonus"))