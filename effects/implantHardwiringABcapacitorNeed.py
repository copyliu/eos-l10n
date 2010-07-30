#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Navigation Implants (3 of 3)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                  "capacitorNeed", implant.getModifiedItemAttr("capNeedBonus"))