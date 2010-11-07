#Used by:
#Ship: Cerberus
#Ship: Sacrilege
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Assault Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Heavy",
                                  "speed", ship.getModifiedItemAttr("eliteBonusHeavyGunship2") * level)
