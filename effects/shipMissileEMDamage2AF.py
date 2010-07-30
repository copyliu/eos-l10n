#Used by:
#Ship: Inquisitor
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "emDamage", ship.getModifiedItemAttr("shipBonus2AF") * level)