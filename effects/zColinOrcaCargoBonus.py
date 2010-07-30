#Item: Orca [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Industrial Command Ships").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("shipOrcaCargoBonusOrca1") * level)