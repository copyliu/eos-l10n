#Item: Proteus Electronics - Dissolution Sequencer [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Electronic Systems").level
    fit.ship.boostItemAttr("maxTargetRange", module.getModifiedItemAttr("subsystemBonusGallenteElectronic2") * level)