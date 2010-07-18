#Item: Mackinaw [Ship]
from customEffects import boostModListBySkillReq
def iceHarvesterMiningAmountBonusMultiplier(self, fitting):
    boostModListBySkillReq(fitting.modules, "miningAmount", 100,
                           lambda skill: skill.name == "Ice Harvesting", self.item)