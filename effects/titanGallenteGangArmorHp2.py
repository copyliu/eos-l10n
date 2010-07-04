#Used by: Ship: Leviathan
type = ("gang", "normal")
from customEffects import boost, multiply
def titanGallenteGangArmorHp2(self, fitting, activeLayer):
    if activeLayer == "ship":
        skill, level = fitting.getCharSkill("Gallente Titan")
        multiply(self.item, "titanGallenteBonus2", level)
        self.item.attributes["commandBonus"] = self.item.attributes["titanGallenteBonus2"]
    else:
        boost(fitting.ship, "armorHP", "titanGallenteBonus2", self.item)