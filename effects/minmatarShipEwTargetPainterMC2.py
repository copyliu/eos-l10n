#Variations of item: Bellicose (3 of 3) [Ship]
from customEffects import boostModListByReq
def minmatarShipEwTargetPainterMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListByReq(fitting.modules, "signatureRadiusBonus", "shipBonusMC2",
                      lambda mod: mod.group.name == "Target Painter",
                      self.item, extraMult = level)