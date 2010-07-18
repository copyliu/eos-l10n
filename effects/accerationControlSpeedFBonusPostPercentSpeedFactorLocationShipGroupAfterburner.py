#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Navigation Implants (3 of 15)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Afterburner",
                                  "speedFactor", implant.getItemAttr("speedFBonus"))