#Used by:
#Variations of ship: Mammoth (2 of 2)
#Variations of ship: Wreathe (2 of 2)
#Ship: Hoarder
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Industrial")
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("shipBonusMI") * level)