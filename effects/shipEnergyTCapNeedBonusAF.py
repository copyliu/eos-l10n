#Used by:
#Variations of ship: Executioner (2 of 3)
#Variations of ship: Magnate (3 of 4)
#Variations of ship: Punisher (2 of 3)
#Ship: Crucifier
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonus2AF") * level)