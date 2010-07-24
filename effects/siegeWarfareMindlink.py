#Item: Siege Warfare Mindlink [Implant]
from customEffects import boostModListBySkillReq
def siegeWarfareMindlink(self, fitting):
    fit.character.getSkill("Siege Warfare").suppress()
    boostModListBySkillReq(fitting.modules, "commandBonus", "mindlinkBonus",
                           lambda skill: skill.name == "Siege Warfare Specialist",
                           self.item)