#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Gunslinger' AX (3 of 3)
#Implant: Ogdin's Eye Coordination Enhancer
#Skill: Motion Prediction
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "trackingSpeed", container.getModifiedItemAttr("trackingSpeedBonus") * level)
