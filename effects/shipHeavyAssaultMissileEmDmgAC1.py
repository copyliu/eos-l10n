#Item: Sacrilege [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "emDamage", ship.getModifiedItemAttr("shipBonusAC") * level)