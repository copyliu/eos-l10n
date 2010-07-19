#Item: Capital Shield Emission Systems [Skill]
#Item: Hardwiring - Zainou 'Sprite' KXX1000 [Implant]
#Item: Hardwiring - Zainou 'Sprite' KXX2000 [Implant]
#Item: Hardwiring - Zainou 'Sprite' KXX500 [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Shield Emission Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)