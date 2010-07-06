#Used by: Item: Memetic Algorithm Bank
#               Hardwiring - 'Prospector' PPX-1
from customEffects import boostModListBySkillReq, increase
def accessDifficultyBonusModifierRequiringHacking(self, fitting, state = None):
    boostModListBySkillReq(fitting.modules, "accessDifficultyBonus",
                           "accessDifficultyBonusModifier",
                           lambda skill: skill.name == "Hacking",
                           self.item, helper = increase)