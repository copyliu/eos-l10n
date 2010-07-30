#Item: Vengeance [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Assault Ships").level
    fit.ship.boostItemAttr("armorEmDamageResonance", ship.getModifiedItemAttr("eliteBonusGunship1") * level)