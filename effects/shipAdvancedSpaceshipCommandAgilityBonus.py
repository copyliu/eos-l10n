#Items from group: Dreadnought (4 of 4) [Ship]
#Items from group: Freighter (4 of 4) [Ship]
#Items from group: Jump Freighter (4 of 4) [Ship]
#Items from group: Titan (4 of 4) [Ship]
#Items from market group: Ships > Carriers (8 of 8)
#Item: Rorqual [Ship]
type = "passive"
def handler(fit, ship, context):
    skill = fit.character.getSkill("Advanced Spaceship Command")
    level = skill.level
    fit.ship.boostItemAttr("agility", skill.getModifiedItemAttr("agilityBonus") * level)