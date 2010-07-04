#Used by: Item: Salvage Tackle
from customEffects import boostModListBySkillReq, increase
def salvagingAccessDifficultyBonusEffectPassive(self, fitting, state):
    boostModListBySkillReq(fitting.modules, "accessDifficultyBonus", "accessDifficultyBonus",
                           lambda skill: skill.name == "Salvaging",
                           self.item, helper = increase)