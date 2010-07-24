#Variations of item: Prophecy (3 of 3) [Ship]
#Item: Malediction [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.ship.boostItemAttr("armorEmDamageResonance", ship.getModifiedItemAttr("shipBonusBC1") * level)