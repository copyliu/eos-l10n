#Used by:
#Ship: Ishtar
type = "passive"
def handler(fit, container, context):
    pass
    level = fit.character.getSkill("Heavy Assault Ships").level
    amount = container.getModifiedItemAttr("eliteBonusHeavyGunship1") * level
    fit.extraAttributes.increase("droneControlRange", amount)
