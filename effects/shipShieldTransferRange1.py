#Item: Basilisk [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Transporter",
                                  "shieldTransferRange", ship.getModifiedItemAttr("shipBonusCC") * level)