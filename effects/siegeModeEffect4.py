#Used by:
#Module: Siege Module I
type = "active"
runTime = "early"
def handler(fit, module, context):
    #Turrets
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "damageMultiplier", module.getModifiedItemAttr("damageMultiplierBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "trackingSpeed", module.getModifiedItemAttr("trackingSpeedBonus"))

    #Missiles
    for type in ("kinetic", "thermal", "explosive", "em"):
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                        "%sDamage" % type, module.getModifiedItemAttr("damageMultiplierBonus"))

    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                     "aoeVelocity", module.getModifiedItemAttr("aoeVelocityBonus"))

    #Shield Boosters
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "duration", module.getModifiedItemAttr("shieldBonusDurationBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "shieldBonus", module.getModifiedItemAttr("shieldBoostMultiplier"))

    #Armor Reppers
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", module.getModifiedItemAttr("armorDamageAmountBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "duration", module.getModifiedItemAttr("armorDamageDurationBonus"))

    #Speed penalty
    fit.ship.multiplyItemAttr("maxVelocity", module.getModifiedItemAttr("speedFactor"))

    #Mass
    fit.ship.multiplyItemAttr("mass", module.getModifiedItemAttr("massMultiplier"))

    #Scan resolution
    fit.ship.multiplyItemAttr("scanResolution", module.getModifiedItemAttr("scanResolutionMultiplier"))

    #Max locked targets
    fit.ship.forceItemAttr("maxLockedTargets", module.getModifiedItemAttr("maxLockedTargets"))

    #Block Hostile EWAR and friendly effects
    fit.ship.forceItemAttr("disallowOffensiveModifiers", module.getModifiedItemAttr("disallowOffensiveModifiers"))
    fit.ship.forceItemAttr("disallowAssistance", module.getModifiedItemAttr("disallowAssistance"))
