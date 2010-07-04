#Used by: Skill: Signature Focusing
from customEffects import boostModListByReq
def ewSkillTargetPaintingStrengthBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "signatureRadiusBonus", "scanSkillTargetPaintStrengthBonus",
                      lambda mod: mod.group.name == "Target Painter",
                      self.item, extraMult = level)