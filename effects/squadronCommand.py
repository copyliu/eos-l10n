#Used by: Skill: Warfare Link Specialist
from customEffects import boostModListByReq
def squadronCommand(self, fitting, level):
    boostModListByReq(fitting.modules, "commandBonus", "squadronCommandBonus",
                      lambda mod: mod.group.name == "Gang Coordinator" and \
                      "commandBonus" in mod.attributes,
                      self.item, extraMult = level)