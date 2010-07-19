#Items from market group: Ships > Carriers > Amarr (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Carrier").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Remote Armor Repair Systems"),
                                  "maxRange", ship.getModifiedItemAttr("carrierAmarrBonus3") * level)
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Energy Emission Systems"),
                                  "powerTransferRange", ship.getModifiedItemAttr("carrierAmarrBonus3") * level)
    