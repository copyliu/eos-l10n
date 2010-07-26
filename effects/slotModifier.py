#Items from category: Subsystem (80 of 80)
def handler(fit, module, context):
    fit.ship.increaseItemAttr("lowSlots", module.getModifiedItemAttr("lowSlotModifier"))
    fit.ship.increaseItemAttr("medSlots", module.getModifiedItemAttr("medSlotModifier"))
    fit.ship.increaseItemAttr("hiSlots", module.getModifiedItemAttr("hiSlotModifier"))