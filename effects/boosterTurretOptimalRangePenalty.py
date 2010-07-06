#Used by: Item: Blue Pill Booster
#               Sooth Sayer Booster
#               Mindflood Booster
from customEffects import boostModListBySkillReq
type = "boosterSideEffect"
def boosterTurretOptimalRangePenalty(self, fitting):
    boostModListBySkillReq(fitting.modules, "maxRange", "boosterTurretOptimalRange",
                           lambda skill: skill.name == "Gunnery", self.item)