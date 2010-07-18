from customEffects import boostModListByReq
def shipBonusStasisMF2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusMF2",
                      lambda mod: mod.group.name == "Stasis Web",
                      self.item, extraMult = level)