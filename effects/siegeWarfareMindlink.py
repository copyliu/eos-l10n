#Item: Siege Warfare Mindlink [Implant]
from customEffects import boostModListBySkillReq
def siegeWarfareMindlink(self, fitting):
    boostModListBySkillReq(fitting.modules, "commandBonus", "mindlinkBonus",
                           lambda skill: skill.name == "Siege Warfare Specialist",
                           self.item)