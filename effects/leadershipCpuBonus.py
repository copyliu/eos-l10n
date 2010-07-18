#Items from group: Battlecruiser (8 of 8)
#Items from group: Carrier (4 of 4)
#Items from group: Command Ship (8 of 8)
#Items from group: Defensive Systems (4 of 16)
#Items from group: Supercarrier (4 of 4)
#Items from group: Titan (4 of 4)
#Item: Orca
#Item: Rorqual
from customEffects import boostModListBySkillReq
def leadershipCpuBonus(self, fitting, state = None):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Leadership", self.item)