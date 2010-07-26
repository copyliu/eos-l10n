#Item: Proteus Offensive - Drone Synthesis Projector [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Offensive Systems").level
    for bonus in ("hp", "armorHP", "shieldCapacity"):
        fit.drones.filteredItemBoost(lambda drone: True, bonus,
                                     module.getModifiedItemAttr("subsystemBonusGallenteOffensive") * level)