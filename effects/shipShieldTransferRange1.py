#Item: Basilisk
from customEffects import boostModListByReq
def shipShieldTransferRange1(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "shieldTransferRange", "shipBonusCC",
                      lambda mod: mod.group.name == "Shield Transporter",
                      self.item, extraMult = level)