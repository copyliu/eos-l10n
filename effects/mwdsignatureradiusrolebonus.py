# Used by:
# Ships from group: Assault Ship (8 of 11)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("High Speed Maneuvering"),
                                  "signatureRadiusBonus", ship.getModifiedItemAttr("MWDSignatureRadiusBonus"))
