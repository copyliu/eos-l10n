#Items with name like: Magnate (3 of 3)
#Variations of item: Executioner (2 of 3) [Ship]
#Variations of item: Punisher (2 of 3) [Ship]
#Item: Crucifier [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonus2AF") * level)