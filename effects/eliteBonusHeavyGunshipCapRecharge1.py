#Item: Sacrilege [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Assault Ships").level
    fit.ship.boostItemAttr("rechargeRate", ship.getModifiedItemAttr("eliteBonusHeavyGunship1") * level)