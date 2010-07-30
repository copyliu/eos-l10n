#Used by:
#Implant: Armored Warfare Mindlink
type = "gang"
runTime = "early"
def handler(fit, module, context):
    fit.character.getSkill("Armored Warfare").suppress()
    fit.ship.boostItemAttr("armorHP", module.getModifiedItemAttr("armorHpBonus2"))