#Used by: Ship: Hulk
#               Mackinaw
from customEffects import boostModListBySkillReq
def eliteBargeBonusIceHarvestingCycleTimeBarge3(self, fitting):
    skill, level = fitting.getCharSkill("Exhumers")
    boostModListBySkillReq(fitting.modules, "duration", "eliteBonusBarge2",
                           lambda skill: skill.name == "Ice Harvesting",
                           self.item, extraMult = level)