#Used by: Skill: Mining
#                Astreology
#         Item : Michi's Excavation Augmentor
#                Hardwiring - 'Highwall' HX-X
from customEffects import boostModListBySkillReq
def astrogeologyMiningAmountBonusPostPercentMiningAmountLocationShipModulesRequiringMining(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "miningAmount", "miningAmountBonus",
                           lambda skill: skill.name == "Mining",
                           self.item, extraMult = level)