#Item: Proteus Electronics - Dissolution Sequencer [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Electronic Systems").level
    fit.ship.boostItemAttr("scanMagnetometricStrength", module.getModifiedItemAttr("subsystemBonusGallenteElectronic") * level)
