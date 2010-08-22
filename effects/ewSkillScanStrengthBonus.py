#Used by:
#Modules named like: Particle Dispersion Augmentor (6 of 6)
#Skill: Signal Dispersion
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM" or mod.item.group.name == "ECM Burst",
                                      "scan{0}StrengthBonus".format(scanType), container.getModifiedItemAttr("scanSkillEwStrengthBonus") * level)
