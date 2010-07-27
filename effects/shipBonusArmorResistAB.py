#Item: Abaddon [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Battleship").level
    for type in ("Explosive", "Kinetic", "Em", "Thermal"):
        fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                        "armor%sDamageResonance" % type,
                                        ship.getModifiedItemAttr("shipBonusAB") * level)