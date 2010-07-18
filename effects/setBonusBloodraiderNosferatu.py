#Items from group: Cyberimplant (10 of 138) [Implant]
from customEffects import boostModListBySkillReq
def setBonusBloodraiderNosferatu(self, fitting):
    boostModListBySkillReq(fitting.modules, "duration", "durationBonus",
                           lambda skill: skill.name == "Energy Emission Systems",
                           self.item)