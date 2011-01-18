#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Rogue' EY (6 of 6)
#Implant: Zor's Custom Navigation Link
#Skill: Afterburner
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                     "duration", container.getModifiedItemAttr("durationBonus") * level)
