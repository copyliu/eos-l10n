#Used by: Item: Capacitor Power Relay
#               Shield Boost Amplifier
from customEffects import boostModListBySkillReq
import model.fitting
def shieldBoostAmplifier(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListBySkillReq(fitting.modules, "shieldBonus", "shieldBoostMultiplier",
                               lambda skill: skill.name in ("Shield Operation", "Capital Shield Operation"),
                               self.item, useStackingPenalty = self.item.group.name == "Shield Boost Amplifier")
