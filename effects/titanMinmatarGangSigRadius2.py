#Item: Ragnarok [Ship]
type = ("gang", "normal")
from customEffects import boost, multiply
def titanMinmatarGangSigRadius2(self, fitting, activeLayer):
    if activeLayer == "ship":
        skill, level = fitting.getCharSkill("Minmatar Titan")
        multiply(self.item, "titanMinmatarBonus2", level)
        self.item.attributes["commandBonus"] = self.item.attributes["titanMinmatarBonus2"]
    else:
        boost(fitting.ship, "signatureRadius", "titanMinmatarBonus2", self.item)