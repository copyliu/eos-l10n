#Used by:
#Ships from group: Covert Ops (4 of 4)
type = "passive"
runTime = "early"
def handler(fit, ship, context):
    level = fit.character.getSkill("Covert Ops").level
    bonus = -ship.getModifiedItemAttr("eliteBonusCoverOps1")
    fit.ship.increaseItemAttr("cloakingCpuNeedBonus", bonus * level)
