#Item: Freki [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Stasis Web",
                                    "maxRange", ship.getModifiedItemAttr("shipBonusMF2") * level)