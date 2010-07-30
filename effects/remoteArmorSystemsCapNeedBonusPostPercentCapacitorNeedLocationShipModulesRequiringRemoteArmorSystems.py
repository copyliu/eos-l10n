#Used by:
#Modules named like: Remote Repair Augmentor (6 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Armor Implants (3 of 3)
#Skill: Remote Armor Repair Systems
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Remote Armor Repair Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
