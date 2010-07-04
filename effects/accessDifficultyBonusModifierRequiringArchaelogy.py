#Used by: Item: Emission Scope Sharpener
#               Hardwiring - 'Prospector' PPW-1
from customEffects import boostModListBySkillReq, increase
def accessDifficultyBonusModifierRequiringArchaelogy(self, fitting, state = None):
    boostModListBySkillReq(fitting.modules, "accessDifficultyBonus",
                           "accessDifficultyBonusModifier",
                           lambda skill: skill.name == "Archaeology",
                           self.item, helper = increase)