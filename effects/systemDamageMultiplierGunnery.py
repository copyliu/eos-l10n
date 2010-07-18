#Items from group: Effect Beacon (6 of 38) [Celestial]
from customEffects import boostModListBySkillReq, multiply
type = "projected"
def systemDamageMultiplierGunnery(self, fitting, state):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierMultiplier",
                      lambda skill: skill.name == "Gunnery",
                      self.item, helper = multiply)