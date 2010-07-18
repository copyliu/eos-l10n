#Items from group: Capacitor Power Relay (25 of 25)
#Items from group: Shield Boost Amplifier (25 of 25)
from customEffects import boostModListBySkillReq
import model.fitting
def shieldBoostAmplifier(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListBySkillReq(fitting.modules, "shieldBonus", "shieldBoostMultiplier",
                               lambda skill: skill.name in ("Shield Operation", "Capital Shield Operation"),
                               self.item, useStackingPenalty = self.item.group.name == "Shield Boost Amplifier")
