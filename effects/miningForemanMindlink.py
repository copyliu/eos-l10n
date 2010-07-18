#Item: Mining Foreman Mindlink
from customEffects import boostModListBySkillReq
def miningForemanMindlink(self, fitting):
    boostModListBySkillReq(fitting.modules, "commandBonus", "mindlinkBonus",
                           lambda skill: skill.name == "Mining Director",
                           self.item)