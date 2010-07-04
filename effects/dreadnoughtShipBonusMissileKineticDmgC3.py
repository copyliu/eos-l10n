#Used by: Ship: Phoenix
from customEffects import boostAmmoListBySkillReq
def dreadnoughtShipBonusMissileKineticDmgC3(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Dreadnought")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "dreadnoughtShipBonusC3",
                            lambda skill: skill.name == "Citadel Cruise Missiles",
                            self.item, extraMult = level)
