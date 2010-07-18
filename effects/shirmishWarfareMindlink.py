#Item: Skirmish Warfare Mindlink
from customEffects import boostModListBySkillReq
def shirmishWarfareMindlink(self, fitting):
    boostModListBySkillReq(fitting.modules, "commandBonus", "mindlinkBonus",
                           lambda skill: skill.name == "Skirmish Warfare Specialist",
                           self.item)