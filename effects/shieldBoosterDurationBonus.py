#Used by: Item: Core Defence Operational Solidifier
from customEffects import boostModListByReq
def shieldBoosterDurationBonus(self, fitting, state):
    boostModListByReq(fitting.modules, "duration", "durationSkillBonus",
                      lambda mod: mod.group.name == "Shield Booster", self.item)