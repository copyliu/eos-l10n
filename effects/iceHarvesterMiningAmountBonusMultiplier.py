#Used by: Ship: Mackinaw
from customEffects import boostModListBySkillReq
def iceHarvesterMiningAmountBonusMultiplier(self, fitting):
    boostModListBySkillReq(fitting.modules, "miningAmount", 100,
                           lambda skill: skill.name == "Ice Harvesting", self.item)