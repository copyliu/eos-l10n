#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Armor Implants (3 of 3)
#Variations of item: Large Remote Repair Augmentor I (2 of 2) [Module]
#Variations of item: Medium Remote Repair Augmentor I (2 of 2) [Module]
#Variations of item: Small Remote Repair Augmentor I (2 of 2) [Module]
#Item: Remote Armor Repair Systems [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Remote Armor Repair Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
