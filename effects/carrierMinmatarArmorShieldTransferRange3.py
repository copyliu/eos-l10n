#Items from market group: Ships > Carriers > Minmatar (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Carrier").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Shield Emission Systems"),
                                  "shieldTransferRange", ship.getModifiedItemAttr("carrierMinmatarBonus3") * level)
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Remote Armor Repair Systems"),
                                  "shieldTransferRange", ship.getModifiedItemAttr("carrierMinmatarBonus3") * level)