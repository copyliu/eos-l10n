#Item: Information Warfare Mindlink [Implant]
from customEffects import boostModListBySkillReq
def informationWarfareMindlinkHidden(self, fitting):
    boostModListBySkillReq(fitting.modules, "commandBonus", "mindlinkBonus",
                           lambda skill: skill.name == "Information Warfare Specialist",
                           self.item)