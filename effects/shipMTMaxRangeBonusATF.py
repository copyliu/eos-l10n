#Item: Freki [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "falloffmaxRange", ship.getModifiedItemAttr("shipBonusATF2"))