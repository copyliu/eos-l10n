#Variations of item: Large Drone Control Range Augmentor I (2 of 2) [Module]
#Variations of item: Medium Drone Control Range Augmentor I (2 of 2) [Module]
#Variations of item: Small Drone Control Range Augmentor I (2 of 2) [Module]
#Item: Electronic Warfare Drone Interfacing [Skill]
#Item: Scout Drone Operation [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.droneControlRange += container.getModifiedItemAttr("droneRangeBonus") * level