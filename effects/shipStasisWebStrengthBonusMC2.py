#Used by: Ship: Vigilant
from customEffects import boostModListByReq
def shipStasisWebStrengthBonusMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListByReq(fitting.modules, "speedFactor", "shipBonusMC2",
                      lambda mod: mod.group.name == "Stasis Web",
                      self.item, extraMult = level)