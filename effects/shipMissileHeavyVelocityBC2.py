#Used by: Ship: Damnation
from customEffects import boostAmmoListBySkillReq
def shipMissileHeavyVelocityBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusBC2",
                       lambda skill: skill.name == "Heavy Missiles",
                       self.item, extraMult = level)