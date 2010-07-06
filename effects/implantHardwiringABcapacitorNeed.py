#Used by: Item: Hardwiring - 'Rogue' DY-1
from customEffects import boostModListBySkillReq
def implantHardwiringABcapacitorNeed(self, fitting):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Afterburner", self.item)