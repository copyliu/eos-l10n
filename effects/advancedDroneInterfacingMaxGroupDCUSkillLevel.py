#Used by: Skill: Advanced Drone Interfacing
from customEffects import boostModListByReq, increase
def advancedDroneInterfacingMaxGroupDCUSkillLevel(self, fitting, level):
    boostModListByReq(fitting.modules, "maxGroupActive", 1,
                      lambda mod: mod.group.name == "Drone Control Unit",
                      self.item, extraMult = level, helper = increase)
