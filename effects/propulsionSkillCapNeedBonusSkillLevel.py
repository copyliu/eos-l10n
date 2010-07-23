#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Electronics Implants (3 of 6)
#Item: Propulsion Jamming [Skill]
type = "passive"
def handler(fit, container, context):
    groups = "Stasis Web", "Warp Scrambler"
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.group.name in groups,
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)