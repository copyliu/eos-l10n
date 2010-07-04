#Used by: Ship: Golem
from customEffects import boostModListByReq
def eliteBonusViolatorsEwTargetPainting1(self, fitting):
    skill, level = fitting.getCharSkill("Marauders")
    boostModListByReq(fitting.modules, "signatureRadiusBonus", "eliteBonusViolators1",
                      lambda mod: mod.group.name == "Target Painter",
                      self.item, extraMult = level)