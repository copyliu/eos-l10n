#Item: Legion Offensive - Drone Synthesis Projector [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Offensive Systems").level
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Combat Drone",
                                 "damageMultiplier", module.getModifiedItemAttr("subsystemBonusAmarrOffensive") * level)
