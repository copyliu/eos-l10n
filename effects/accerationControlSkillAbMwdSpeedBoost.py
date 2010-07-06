#Used by: Skill: Acceleration Control
from customEffects import boostModListByReq
def accerationControlSkillAbMwdSpeedBoost(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "speedFactor", "speedFBonus",
                      lambda mod: mod.group.name == "Afterburner",
                      self.item, extraMult = level)