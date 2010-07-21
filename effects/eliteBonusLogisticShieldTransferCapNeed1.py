#Item: Basilisk [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Logistics").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Transporter",
                                  "capacitorNeed", ship.getModifiedItemAttr("eliteBonusLogistics1") * level)