#Items with name like: Slave (10 of 12)
#Items with name like: Trimark Armor Pump (6 of 6)
#Item: Hull Upgrades [Skill]
#Item: Low-grade Snake Epsilon [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("armorHP", container.getModifiedItemAttr("armorHpBonus") * level)
