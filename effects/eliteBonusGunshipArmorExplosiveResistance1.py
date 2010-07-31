#Used by:
#Ship: Vengeance
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Assault Ships").level
    fit.ship.boostItemAttr("armorExplosiveDamageResonance", ship.getModifiedItemAttr("eliteBonusGunship1") * level)