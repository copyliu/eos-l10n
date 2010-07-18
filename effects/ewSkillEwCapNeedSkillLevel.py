#Items from group: Cyber Electronics (3 of 27)
#Items from group: Rig Electronics (6 of 30)
#Item: Electronic Warfare
from customEffects import boostModListByReq
def ewSkillEwCapNeedSkillLevel(self, fitting, state = None, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)
