#Item: Signature Focusing [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Target Painter",
                                  "signatureRadiusBonus", skill.getModifiedItemAttr("scanSkillTargetPaintStrengthBonus") * skill.level)