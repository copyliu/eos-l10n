# Used by:
# Ships from group: Transport Ship (4 of 8)
type = "passive"
runTime = "early"
def handler(fit, ship, context):
    level = fit.character.getSkill("Transport Ships").level
    bonus = ship.getModifiedItemAttr("eliteIndustrialCovertCloakBonus")
    fit.ship.boostItemAttr("cloakingCpuNeedBonus", bonus * level)
