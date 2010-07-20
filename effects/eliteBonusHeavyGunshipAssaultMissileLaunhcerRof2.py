#Item: Cerberus [Ship]
#Item: Sacrilege [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Assault Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Missile Launcher Assault",
                                  "speed", ship.getModifiedItemAttr("eliteBonusHeavyGunship2") * level)