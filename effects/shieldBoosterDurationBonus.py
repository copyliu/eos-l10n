#Variations of item: Large Core Defence Operational Solidifier I (2 of 2)
#Variations of item: Medium Core Defence Operational Solidifier I (2 of 2)
#Variations of item: Small Core Defence Operational Solidifier I (2 of 2)
from customEffects import boostModListByReq
def shieldBoosterDurationBonus(self, fitting, state):
    boostModListByReq(fitting.modules, "duration", "durationSkillBonus",
                      lambda mod: mod.group.name == "Shield Booster", self.item)