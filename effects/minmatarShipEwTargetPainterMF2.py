#Variations of item: Vigil (2 of 2)
from customEffects import boostModListByReq
def minmatarShipEwTargetPainterMF2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListByReq(fitting.modules, "signatureRadiusBonus", "shipBonusMF2",
                      lambda mod: mod.group.name == "Target Painter",
                      self.item, extraMult = level)