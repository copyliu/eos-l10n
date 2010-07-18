#Items from group: Effect Beacon (6 of 38)
type = "projected"
from customEffects import multiply, boostModListBySkillReq
def systemSmallHybridDamage(self, fitting, state):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "smallWeaponDamageMultiplier",
                           lambda skill: skill.name == "Small Hybrid Turret", self.item,
                           helper = multiply)