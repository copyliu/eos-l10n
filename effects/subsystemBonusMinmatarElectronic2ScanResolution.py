#Item: Loki Electronics - Tactical Targeting Network [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Electronic Systems").level
    fit.ship.boostItemAttr("scanResolution", module.getModifiedItemAttr("subsystemBonusMinmatarElectronic2") * level)