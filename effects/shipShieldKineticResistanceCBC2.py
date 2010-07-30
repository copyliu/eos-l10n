#Variations of item: Ferox (3 of 3) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.ship.boostItemAttr("shieldKineticDamageResonance", ship.getModifiedItemAttr("shipBonusBC2") * level)