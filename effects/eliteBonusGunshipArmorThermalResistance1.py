# Used by:
# Ship: Vengeance
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Assault Ships").level
    fit.ship.boostItemAttr("armorThermalDamageResonance", ship.getModifiedItemAttr("eliteBonusGunship1") * level)