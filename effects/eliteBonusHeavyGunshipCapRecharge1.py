#Used by:
#Ship: Sacrilege
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Assault Ships").level
    fit.ship.boostItemAttr("rechargeRate", ship.getModifiedItemAttr("eliteBonusHeavyGunship1") * level)
