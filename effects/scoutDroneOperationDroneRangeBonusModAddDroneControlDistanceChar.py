#Items with name like: Drone Control Range Augmentor (6 of 6)
#Item: Electronic Warfare Drone Interfacing [Skill]
#Item: Scout Drone Operation [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    amount = container.getModifiedItemAttr("droneRangeBonus")
    fit.extraAttributes["droneControlRange"].increase(amount * level)
