#Items with name like: Halo (10 of 12)
#Items with name like: X-Instinct Booster (4 of 4)
type = "passive"
def handler(fit, implant, context):
    fit.ship.multiplyItemAttr("signatureRadius", implant.getModifiedItemAttr("signatureRadiusBonus"))