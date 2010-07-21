#Variations of item: Large Particle Dispersion Augmentor I (2 of 2) [Module]
#Variations of item: Medium Particle Dispersion Augmentor I (2 of 2) [Module]
#Variations of item: Small Particle Dispersion Augmentor I (2 of 2) [Module]
#Item: Signal Dispersion [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
        fit.modules.filteredItemBoost(lambda mod: mod.group.name == "ECM" or mod.group.name == "ECM Burst",
                                      "scan%sStrengthBonus" % scanType, container.getModifiedItemAttr("scanSkillEwStrengthBonus") * level)