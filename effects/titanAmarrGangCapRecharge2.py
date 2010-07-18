#Item: Avatar
type = ("gang", "normal")
from customEffects import boost, multiply
def titanAmarrGangCapRecharge2(self, fitting, activeLayer):
    if activeLayer == "ship":
        skill, level = fitting.getCharSkill("Amarr Titan")
        multiply(self.item, "titanAmarrBonus2", level)
        self.item.attributes["commandBonus"] = self.item.attributes["titanAmarrBonus2"]
    else:
        boost(fitting.ship, "rechargeRate", "titanAmarrBonus2", self.item)