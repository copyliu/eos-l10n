#Item: Guardian-Vexor [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    amount = ship.getModifiedItemAttr("shipBonusGC2")
    fit.extraAttributes["maxActiveDrones"].increase(amount * level)