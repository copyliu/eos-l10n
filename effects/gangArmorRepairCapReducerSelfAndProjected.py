#Used by:
#Module: Armored Warfare Link - Damage Control
type = "gang", "active"
def handler(fit, module, context):
    if "gang" not in context: return
    groups = ("Armor Repair Unit", "Armor Repair Projector")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "capacitorNeed", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
