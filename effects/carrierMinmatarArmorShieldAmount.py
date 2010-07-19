#Items from market group: Ships > Carriers > Minmatar (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Carrier").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Transporter",
                                  "shieldBonus", ship.getModifiedItemAttr("carrierMinmatarBonus2") * level)
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Projector",
                                  "armorDamageAmount", ship.getModifiedItemAttr("carrierMinmatarBonus2") * level)