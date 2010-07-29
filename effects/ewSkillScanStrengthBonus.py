#Items with name like: Particle Dispersion Augmentor (6 of 6)
#Item: Signal Dispersion [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM" or mod.item.group.name == "ECM Burst",
                                      "scan%sStrengthBonus" % scanType, container.getModifiedItemAttr("scanSkillEwStrengthBonus") * level)
