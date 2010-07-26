#Item: Hardwiring - Eifyr and Co. 'Gunslinger' AX-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' AX-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' AX-2 [Implant]
#Item: Motion Prediction [Skill]
#Item: Ogdin's Eye Coordination Enhancer [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "trackingSpeed", container.getModifiedItemAttr("trackingSpeedBonus") * level)