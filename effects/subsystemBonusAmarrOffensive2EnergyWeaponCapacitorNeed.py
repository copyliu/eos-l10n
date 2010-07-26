#Item: Legion Offensive - Drone Synthesis Projector [Subsystem]
#Item: Legion Offensive - Liquid Crystal Magnifiers [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "capacitorNeed", module.getModifiedItemAttr("subsystemBonusAmarrOffensive2") * level)