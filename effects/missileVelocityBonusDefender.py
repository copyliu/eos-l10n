#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Missile Implants (3 of 6)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Defender Missiles"),
                                       "maxVelocity", container.getModifiedItemAttr("missileVelocityBonus"))