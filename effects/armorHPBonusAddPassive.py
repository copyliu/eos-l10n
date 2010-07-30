#Items from group: Defensive Systems (16 of 16) [Subsystem]
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("armorHP", module.getModifiedItemAttr("armorHPBonusAdd"))