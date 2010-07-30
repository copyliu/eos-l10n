#Used by:
#Ship: Caldari Navy Hookbill
#Ship: Kestrel
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "emDamage", ship.getModifiedItemAttr("shipBonusCF2") * level)