#Variations of item: Bestower (2 of 2) [Ship]
#Variations of item: Sigil (2 of 2) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Industrial")
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("shipBonusAI") * level)