#Used by:
#Ships from group: Carrier (4 of 4)
#Ships from group: Dreadnought (4 of 4)
#Ships from group: Freighter (4 of 4)
#Ships from group: Jump Freighter (4 of 4)
#Ships from group: Supercarrier (4 of 4)
#Ships from group: Titan (4 of 4)
#Ship: Rorqual
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Advanced Spaceship Command").level
    fit.ship.boostItemAttr("agility", ship.getModifiedItemAttr("agilityBonus") * level)