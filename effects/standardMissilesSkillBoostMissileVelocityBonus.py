#Item: Defender Missiles [Skill]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Defender Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("missileVelocityBonus") * skill.level)