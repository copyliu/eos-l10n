#Used by:
#Ship: Ishtar
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Assault Ships").level
    amount = ship.getModifiedItemAttr("eliteBonusHeavyGunship1") * level
    fit.extraAttributes.increase("droneControlRange", amount)
