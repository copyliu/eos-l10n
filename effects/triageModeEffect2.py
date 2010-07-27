#Item: Triage Module I [Module]
type = "active"
def handler(fit, module, context):
    #Remote armor reps
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Remote Armor Repair Systems"),
                                  "duration", module.getModifiedItemAttr("remoteArmorDamageDurationBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Remote Armor Repair Systems"),
                                  "armorDamageAmount", module.getModifiedItemAttr("remoteArmorDamageAmountBonus"))
    
    #Remote hull reppers
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Remote Hull Repair Systems"),
                                  "structureDamageAmount", module.getModifiedItemAttr("remoteHullDamageAmountBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Remote Hull Repair Systems"),
                                  "duration", module.getModifiedItemAttr("remoteHullDamageDurationBonus"))
    
    #Shield Transporters
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Shield Emission Systems"),
                                  "shieldBonus", module.getModifiedItemAttr("shieldTransportAmountBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Shield Emission Systems"),
                                  "duration", module.getModifiedItemAttr("shieldTransportDurationBonus"))
    
    #Energy Transfer Arrays
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Energy Emission Systems"),
                                  "powerTransferAmount", module.getModifiedItemAttr("powerTransferAmountBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Energy Emission Systems"),
                                  "duration", module.getModifiedItemAttr("powerTransferDurationBonus"))
    
    #Shield boosters
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "shieldBonus", module.getModifiedItemAttr("shieldBoostMultiplier"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "duration", module.getModifiedItemAttr("shieldBonusDurationBonus"))
    
    #Armor reps
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", module.getModifiedItemAttr("armorDamageAmountBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "duration", module.getModifiedItemAttr("armorDamageDurationBonus"))
    
    #Speed bonus
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("speedFactor"))
    
    #Mass multiplier
    fit.ship.multiplyItemAttr("mass", module.getModifiedItemAttr("massMultiplier"))
    
    #Max locked targets
    fit.ship.increaseItemAttr("maxLockedTargets", module.getModifiedItemAttr("maxLockedTargetsBonus"))
    
    #Block EWAR & projected effects
    fit.ship.itemModifiedAttributes["disallowOffensiveModifiers"] = module.getModifiedItemAttr("disallowOffensiveModifiers")
    fit.ship.itemModifiedAttributes["disallowAssistance"] = module.getModifiedItemAttr("disallowAssistance")
