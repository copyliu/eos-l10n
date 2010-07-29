#Item: Hardwiring - Inherent Implants 'Yeti' BX-0 [Implant]
#Item: Hardwiring - Inherent Implants 'Yeti' BX-1 [Implant]
#Item: Hardwiring - Inherent Implants 'Yeti' BX-2 [Implant]
#Item: Ice Harvesting [Skill]
#Item: Mackinaw [Ship]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Ice Harvesting"),
                                  "duration", container.getModifiedItemAttr("iceHarvestCycleBonus") * level)
