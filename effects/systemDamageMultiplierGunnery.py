#Used by: Item: Magnatar Effect Beacon
from customEffects import boostModListBySkillReq, multiply
type = "projected"
def systemDamageMultiplierGunnery(self, fitting, state):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierMultiplier",
                      lambda skill: skill.name == "Gunnery",
                      self.item, helper = multiply)