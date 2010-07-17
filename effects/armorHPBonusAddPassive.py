type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("armorHP", module.getModifiedItemAttr("armorHPBonusAdd"))