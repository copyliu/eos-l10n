#Item: Legion Offensive - Drone Synthesis Projector [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Offensive Systems").level
    for type in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: True, type,
                                     module.getModifiedItemAttr("subsystemBonusAmarrOffensive3") * level)