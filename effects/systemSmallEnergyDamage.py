#Used by: Item: Wolf Rayet Effect Beacon
type = "projected"
from customEffects import multiply, boostModListBySkillReq
def systemSmallEnergyDamage(self, fitting, state):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "smallWeaponDamageMultiplier",
                           lambda skill: skill.name == "Small Energy Turret", self.item,
                           helper = multiply)