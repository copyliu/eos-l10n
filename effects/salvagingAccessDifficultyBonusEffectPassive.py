#Variations of item: Large Salvage Tackle I (2 of 2)
#Variations of item: Medium Salvage Tackle I (2 of 2)
#Variations of item: Small Salvage Tackle I (2 of 2)
#Item: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPY-1
from customEffects import boostModListBySkillReq, increase
def salvagingAccessDifficultyBonusEffectPassive(self, fitting, state):
    boostModListBySkillReq(fitting.modules, "accessDifficultyBonus", "accessDifficultyBonus",
                           lambda skill: skill.name == "Salvaging",
                           self.item, helper = increase)