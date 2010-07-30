#Variations of item: Prophecy (3 of 3) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.ship.boostItemAttr("armorKineticDamageResonance", ship.getModifiedItemAttr("shipBonusBC1") * level)