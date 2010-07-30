#Used by:
#Variations of ship: Magnate (3 of 4)
#Ship: Crucifier
#Ship: Crusader
#Ship: Executioner
#Ship: Punisher
#Ship: Retribution
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonus2AF") * level)