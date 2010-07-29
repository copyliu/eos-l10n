#Items from group: Cyberimplant (11 of 138) [Implant]
#Variations of item: Large Trimark Armor Pump I (2 of 2) [Module]
#Variations of item: Medium Trimark Armor Pump I (2 of 2) [Module]
#Variations of item: Small Trimark Armor Pump I (2 of 2) [Module]
#Item: Hull Upgrades [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("armorHP", container.getModifiedItemAttr("armorHpBonus") * level)
