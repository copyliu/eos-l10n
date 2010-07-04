#Used by: Item: Talisman Implant Set
from customEffects import boostModListBySkillReq
def setBonusBloodraiderNosferatu(self, fitting):
    boostModListBySkillReq(fitting.modules, "duration", "durationBonus",
                           lambda skill: skill.name == "Energy Emission Systems",
                           self.item)