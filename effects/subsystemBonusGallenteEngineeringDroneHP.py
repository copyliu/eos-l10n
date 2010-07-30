#Used by:
#Subsystem: Proteus Engineering - Augmented Capacitor Reservoir
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Engineering Systems").level
    for bonus in ("hp", "armorHP", "shieldCapacity"):
        fit.drones.filteredItemBoost(lambda drone: True, bonus,
                                     module.getModifiedItemAttr("subsystemBonusGallenteEngineering") * level)
