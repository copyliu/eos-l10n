#Used by: Ship: Osprey
from customEffects import boostModListByReq
def shipBonusShieldTransferCapneed1(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "capacitorNeed", "shipBonusCC",
                      lambda mod: mod.group.name == "Shield Transporter",
                      self.item, extraMult = level)
