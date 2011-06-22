# Used by:
# Ships from group: Force Recon Ship (4 of 4)
type = "passive"
runTime = "early"
def handler(fit, ship, context):
    level = fit.character.getSkill("Recon Ships").level
    bonus = -ship.getModifiedItemAttr("eliteBonusReconShip1")
    fit.ship.increaseItemAttr("cloakingCpuNeedBonus", bonus * level)
