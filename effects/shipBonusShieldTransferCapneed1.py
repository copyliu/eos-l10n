#Item: Osprey [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name == "Shield Transporter",
                                    "capacitorNeed", ship.getModifiedItemAttr("shipBonusCC") * level)