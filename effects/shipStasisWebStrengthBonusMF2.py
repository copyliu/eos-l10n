#Item: Cruor [Ship]
#Item: Daredevil [Ship]
from customEffects import boostModListByReq
def shipStasisWebStrengthBonusMF2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListByReq(fitting.modules, "speedFactor", "shipBonusMF2",
                      lambda mod: mod.group.name == "Stasis Web",
                      self.item, extraMult = level)