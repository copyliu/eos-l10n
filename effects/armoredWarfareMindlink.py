#Used by: Armored Warfare Mindlink
from customEffects import boostModListBySkillReq
def armoredWarfareMindlink(self, fitting):
    boostModListBySkillReq(fitting.modules, "commandBonus", "mindlinkBonus",
                           lambda skill: skill.name == "Armored Warfare Specialist",
                           self.item)