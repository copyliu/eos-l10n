#Item: Bhaalgorn
from customEffects import boostModListByReq
def shipStasisWebRangeBonusMB(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusMB",
                      lambda mod: mod.group.name == "Stasis Web",
                      self.item, extraMult = level)