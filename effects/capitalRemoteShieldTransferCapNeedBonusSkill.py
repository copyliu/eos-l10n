#Used by:
#Implants named like: Hardwiring Zainou 'Sprite' KXX (3 of 3)
#Skill: Capital Shield Emission Systems
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Shield Emission Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
