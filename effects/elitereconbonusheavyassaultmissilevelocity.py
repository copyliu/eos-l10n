# Used by:
# Ship: Rook
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Recon Ships").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Assault Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("eliteBonusReconShip1") * level)
