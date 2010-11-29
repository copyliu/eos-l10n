#Used by:
#Items from market group: Ships > Capital Ships (25 of 26)
type = "passive"
def handler(fit, ship, context):
    skill = fit.character.getSkill("Advanced Spaceship Command")
    fit.ship.boostItemAttr("agility", skill.getModifiedItemAttr("agilityBonus") * skill.level)
