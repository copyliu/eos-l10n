#Used by: Ship: Scimitar
from customEffects import boostModListByReq
def shipShieldTransferRange2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusMC2",
                      lambda mod: mod.group.name == "Shield Transporter",
                      self.item, extraMult = level)