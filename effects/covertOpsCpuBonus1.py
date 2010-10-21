#Used by:
#Ships from group: Covert Ops (4 of 4)
#Ships from group: Force Recon Ship (4 of 4)
#Ships from group: Stealth Bomber (4 of 4)
#Ships from group: Transport Ship (4 of 8)
#Subsystems named like: Offensive Covert Reconfiguration (4 of 4)
type = "passive"
def handler(fit, container, context):
    # Cloak CPU consumption static multiplier
    staticBonus = container.getModifiedItemAttr("cloakingCpuNeedBonus")
    containerGroup = container.item.group.name

    # Map of items which are affected
    # { container group : ( bonus skill, bonus per level) }
    cloakyItems = { "Transport Ship" : ("Transport Ships", 0.0015),
                        "Covert Ops" : ("Covert Ops", 0.005),
                  "Force Recon Ship" : ("Recon Ships", 0.01),
                    "Stealth Bomber" : None,
                 "Offensive Systems" : None }

    if containerGroup in cloakyItems:
        data = cloakyItems[containerGroup]
        lvl = fit.character.getSkill(data[0]).level if data else 0
        lvlBonus = data[1] if data else 0
    else:
        lvl = 0
        lvlBonus = 0
        print "Warning: unsupported cloaking device CPU bonus carrier: {0} ({1})".format(container.item.name, containerGroup)

    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Cloaking Device",
                                     "cpu", staticBonus - (lvlBonus * lvl))
