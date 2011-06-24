# Used by:
# Ship: Magnate
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Survey Probe",
                                    "explosionDelay", ship.getModifiedItemAttr("shipBonus3AF") * level)
