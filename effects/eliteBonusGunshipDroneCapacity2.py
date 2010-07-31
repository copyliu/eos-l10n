#Used by:
#Ship: Ishkur
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Assault Ships").level
    fit.ship.increaseItemAttr("droneCapacity", ship.getModifiedItemAttr("eliteBonusGunship2") * level)