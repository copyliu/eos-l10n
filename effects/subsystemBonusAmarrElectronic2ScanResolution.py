#Item: Legion Electronics - Tactical Targeting Network [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Electronic Systems").level
    fit.ship.boostItemAttr("scanResolution", module.getModifiedItemAttr("subsystemBonusAmarrElectronic2") * level)
