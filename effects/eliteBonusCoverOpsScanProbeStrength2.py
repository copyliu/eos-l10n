#Items from group: Covert Ops (4 of 4) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Covert Ops").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Scanner Probe",
                                    "baseSensorStrength", ship.getModifiedItemAttr("eliteBonusCoverOps2") * level)