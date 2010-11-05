#Used by:
#Variations of ship: Heron (2 of 2)
#Ship: Caldari Navy Hookbill
#Ship: Condor
#Ship: Crow
#Ship: Hawk
#Ship: Kestrel
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "kineticDamage", ship.getModifiedItemAttr("shipBonusCF") * level)
