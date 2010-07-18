#Item: Phoenix
from customEffects import boostAmmoListBySkillReq
def dreadnoughtShipBonusMissileKineticDmgC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Dreadnought")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "dreadnoughtShipBonusC2",
                            lambda skill: skill.name == "Citadel Torpedoes",
                            self.item, extraMult = level)
