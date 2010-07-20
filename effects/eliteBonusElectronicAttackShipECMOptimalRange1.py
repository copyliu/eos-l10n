#Item: Kitsune [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Electronic Attack Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "ECM",
                                  "maxRange", ship.getModifiedItemAttr("eliteBonusElectronicAttackShip1") * level)