#Item: Guardian-Vexor [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.maxActiveDrones += ship.getModifiedItemAttr("shipBonusGC2") * level