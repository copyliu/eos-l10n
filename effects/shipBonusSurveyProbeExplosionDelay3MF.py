#Item: Probe [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Survey Probe",
                                    "explosionDelay", ship.getModifiedItemAttr("shipBonus3MF") * level)