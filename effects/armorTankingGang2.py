#Item: Armored Warfare Mindlink [Implant]
type = "gang"
runTime = "early"
def handler(fit, module, context):
    fit.character.getSkill("Armored Warfare").suppress()
    fit.ship.boostItemAttr("armorHP", module.getModifiedItemAttr("armorHpBonus2"))