#Item: Orca [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Industrial Command Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining Director"),
                                  "commandBonus", ship.getModifiedItemAttr("shipOrcaCargoBonusOrca1") * level)