#Used by:
#Ship: Revenant
type = "passive"
def handler(fit, ship, context):
    fit.ship.boostItemAttr("jumpDriveRange", ship.getModifiedItemAttr("shipBonusPirateFaction"))
