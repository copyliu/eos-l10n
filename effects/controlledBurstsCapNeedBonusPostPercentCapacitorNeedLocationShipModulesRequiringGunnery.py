#Item: Controlled Bursts [Skill]
#Item: Hardwiring - Inherent Implants 'Lancer' G0-Beta [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Beta [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Beta [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
